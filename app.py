import torch
import random
import os
import torch.nn as nn
import pandas as pd
import numpy as np
from flask import Flask, request
from torch import stack
from flask.json import jsonify
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
from utils.generic_utils import load_config,Mish
from utils.audio_processor import AudioProcessor 
from utils.dataset import Dataset, test_dataloader, teste_collate_fn
from models.spiraconv import SpiraConvV2
from datetime import datetime


app = Flask(__name__)
model = None
dataloader = None


@app.route('/predict', methods=['POST'])
def predict():
    #guarda o audio e gera o dataloader
    
    nome = datetime.now()
    request.files['audio'].save(f"../resources/audio/{nome}.wav")
    sexo = request.form['sexo']
    idade = request.form['idade']
    nivel = request.form['nivel_falta_de_ar']
    
    csv_file = open("../resources/datasets/input.csv","w")
    csv_file.write(f"file_path,class,sexo,idade,nivel_falta_de_ar\n../audio/{nome}.wav,0,{sexo},{idade},{nivel}")
    csv_file.close()

    #inferência
    dataloader = test_dataloader(c, ap, max_seq_len=max_seq_len)
    with torch.inference_mode():
        for feature, target, slices, targets_org in dataloader:
            output = model.forward(feature)         
            prob = np.average(output)
            result = ""
            if(prob > 0.55):
                result = "Insuficiência respiratória"
            elif(prob > 0.45 and prob < 0.55):
                result = "Inconclusivo"
            else:
                result = "Saudável"
    
        return jsonify({'resultado': result, 'probabilidade': f"{prob}"})

if __name__=="__main__":
    c = load_config("config.json")
    ap = AudioProcessor(**c.audio)
    max_seq_len = c.dataset['max_seq_len'] 

    model = SpiraConvV2(c,ap)
    model.load_state_dict(
        torch.load(os.path.abspath("../checkpoints/spira-chekpoints/spiraconv_v2/best_checkpoint.pt")),
        strict=False)
    model.zero_grad()
    model.eval()

    app.run()
