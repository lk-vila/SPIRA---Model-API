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
from utils.dataset import Dataset, inf_dataloader, test_dataloader
from models.spiraconv import SpiraConvV2
from datetime import datetime
import csv


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    nome = datetime.now()
    request.files['audio'].save(f"./resources/audio/{nome}.wav")
    sexo = request.form['sexo']
    idade = request.form['idade']
    nivel = request.form['nivel_falta_de_ar']
    
    with open('./resources/datasets/input.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['file_path', 'class', 'sexo', 'idade', 'nivel_falta_de_ar'])
        writer.writerow([f'../audio/{nome}.wav', '0', sexo, idade, nivel])

    dataloader = inf_dataloader(config, audio_processor, max_seq_len=max_seq_len)
    with torch.inference_mode():
        for feature, target, slices, targets_org in dataloader:
            output = model(feature)         
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
    config = load_config("config.json")
    audio_processor = AudioProcessor(**config.audio)
    max_seq_len = config.dataset['max_seq_len'] 

    model = SpiraConvV2(config, audio_processor)
    model.load_state_dict(torch.load(os.path.abspath("./resources/checkpoints/spira-checkpoints/spiraconv_v2/best_checkpoint.pt"), map_location=torch.device('cpu')), strict=False)
    #model.zero_grad()
    model.eval()

    app.run()
