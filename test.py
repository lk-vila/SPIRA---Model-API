import torch
import random
import os
import torch.nn as nn
import pandas as pd
import numpy as np
from flask import Flask
from torch import stack
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
from utils.generic_utils import load_config,Mish
from utils.audio_processor import AudioProcessor 
from utils.dataset import Dataset, test_dataloader, teste_collate_fn
from models.spiraconv import SpiraConvV2


#app = Flask(__name__)

if __name__=="__main__":
    #app.run()

    c = load_config("config.json")
    ap = AudioProcessor(**c.audio)
    max_seq_len = c.dataset['max_seq_len'] 

    model = SpiraConvV2(c,ap)
    model.load_state_dict(
        torch.load(os.path.abspath("../checkpoints/spira-chekpoints/spiraconv_v2/best_checkpoint.pt")),
        strict=False)
    model.zero_grad()
    model.eval()

    threshold=0.5
    test_dataloader = test_dataloader(c, ap, max_seq_len=max_seq_len)
    with torch.inference_mode():
        for feature, target, slices, targets_org in test_dataloader:
            output = model.forward(feature)
            print(output)
            if np.average(output) > threshold:
                print("Insuficiencia")
            else:
                print("Saudavel")

