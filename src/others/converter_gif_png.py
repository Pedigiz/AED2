from PIL import Image
import os

def extrair_frames_gif(arquivo_gif, pasta_saida):
    os.makedirs(pasta_saida, exist_ok=True)  
    gif = Image.open(arquivo_gif)
    
    for frame in range(gif.n_frames):
        gif.seek(frame)
        gif.save(os.path.join(pasta_saida, f"{frame}.png"))

extrair_frames_gif("174.gif", "sprites_extraidos")
