import os 

PATH = 'C:/Users/humbe/Documents'
def get_fichier():
    return os.listdir(path= PATH)

def know_fichier(file_list:list):

    for file in file_list:
        concat = PATH
        if os.path.splitext(file)[1]:
            concat+= f'/{file}' 
            size = os.path.getsize(concat)
            print(f'Archivo: {file} Tamaño: {size} B')


know_fichier(get_fichier())