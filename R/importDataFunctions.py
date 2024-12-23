import pandas as pd

def import_data_swow(data_file, response):
    X = pd.read_csv(data_file, header=0, sep=",", encoding="utf-8")
    
    # Convertir a formato largo
    X = pd.melt(X, id_vars=['cue'], value_vars=['R1', 'R2', 'R3'], 
                var_name='RPOS', value_name='response')
    
    # Remover palabras británicas
    X = remove_brexit_words(X)
    
    # Filtrar según respuesta
    if response == 'R1':
        X = X[X['RPOS'] == 'R1']
    elif response == 'R2':
        X = X[X['RPOS'] == 'R2']
    elif response == 'R3':
        X = X[X['RPOS'] == 'R3']
    elif response == 'R12':
        X = X[X['RPOS'].isin(['R1', 'R2'])]
    
    return X

def remove_brexit_words(X):
    UK_words = [
        'aeroplane', 'arse', 'ax', 'bandana', 'bannister', 'behaviour', 
        'bellybutton', 'centre', 'cheque', 'chilli', 'colour', 'harbour',
        'pyjamas', 'neighbour', 'organisation', 'realise', 'theatre', 
        'whisky', 'yoghurt', 'lollypop', 'smokey', 'bubble gum'
    ]
    return X[~X['cue'].isin(UK_words)]
