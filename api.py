import torch
import os
from flask import Flask, request
from waitress import serve
from flask.json import jsonify
from utils.generic_utils import load_config
from utils.audio_processor import AudioProcessor 
from utils.dataset import inf_dataloader, test_dataloader
from utils.custom_logger import getCustomLogger
from models.spiraconv import SpiraConvV2
from datetime import datetime
import csv


logger = getCustomLogger("waitress")

config = load_config("config/spira.json")
audio_processor = AudioProcessor(**config.audio)
max_seq_len = config.dataset['max_seq_len']
model = SpiraConvV2(config, audio_processor)
model.load_state_dict(torch.load(os.path.abspath(
    "./resources/checkpoints/spira-checkpoints/spiraconv_v2/best_checkpoint.pt"), map_location='cpu')['model'], strict=True)
model.zero_grad()
model.eval()

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():    
    nome = datetime.now()
    request.files['audio'].save(f"./resources/audio/{nome}.wav")
    sexo = request.form['sexo']
    idade = request.form['idade']
    nivel = request.form['nivel_falta_de_ar']
       
    logger.info((f"audio = {request.files['audio']} {type(request.files['audio'])} | sexo = {sexo} | idade = {idade} | nivel = {nivel}"))
    
    with open('./resources/datasets/input.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['file_path', 'class', 'sexo', 'idade', 'nivel_falta_de_ar'])
        writer.writerow([f'../audio/{nome}.wav', '0', sexo, idade, nivel])

    dataloader = inf_dataloader(config, audio_processor, max_seq_len=max_seq_len)
    with torch.inference_mode():
        for feature, target, slices, targets_org in dataloader:
            # unpack overlapping for calculation loss and accuracy 
            output = model(feature).float()

            if slices is not None and targets_org is not None:
                idx = 0
                new_output = []
                new_target = []
                for i in range(slices.size(0)):
                    num_samples = int(slices[i].cpu().numpy())

                    samples_output = output[idx:idx+num_samples]
                    output_mean = samples_output.mean()
                    samples_target = target[idx:idx+num_samples]
                    target_mean = samples_target.mean()

                    new_target.append(target_mean)
                    new_output.append(output_mean)
                    idx += num_samples

                target = torch.stack(new_target, dim=0)
                output = torch.stack(new_output, dim=0)

        os.remove(f"./resources/audio/{nome}.wav")


        result = output[0].item()

        logger.info((f"{round(result, 3)}"))
        
        return jsonify({'resultado': f"{round(result, 3)}"})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=(os.getenv("PORT") or 5000))