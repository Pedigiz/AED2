from PIL import Image
import os

def split_image(image_path):
    # Abre a imagem
    img = Image.open(image_path)
    
    # Obtém as dimensões da imagem
    img_width, img_height = img.size
    
    # Define as dimensões dos cortes
    slice_width = 48
    slice_height = 64
    
    # Calcula quantos cortes podem ser feitos
    num_slices = img_width // slice_width
    
    # Cria uma pasta para armazenar as imagens cortadas
    output_folder = "slices"
    os.makedirs(output_folder, exist_ok=True)
    
    # Itera e salva cada fatia
    for i in range(num_slices):
        left = i * slice_width
        upper = 0
        right = left + slice_width
        lower = slice_height
        
        slice_img = img.crop((left, upper, right, lower))
        slice_img.save(os.path.join(output_folder, f"{i+1}.png"))
    
    print(f"Imagem dividida em {num_slices} partes e salva na pasta '{output_folder}'.")

# Exemplo de uso
split_image("walk_Up.png")
