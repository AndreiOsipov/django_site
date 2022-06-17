import os
import base64

def generate_image_list(key_word):
    string_image_list = []
    this_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(this_dir, 'static/generator/images')
    files = os.listdir(path=path)
    for i in range(len(files)):
        full_path = os.path.join(path, files[i])
        with open(full_path, "rb") as image_file:
            string_image_list.append(base64.b64encode(image_file.read()).decode('utf-8'))
    return string_image_list