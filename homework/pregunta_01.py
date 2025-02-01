# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

import os
import zipfile
import pandas as pd


def pregunta_01():
    # Descomprimir el archivo input.zip (ubicado en files/input.zip)
    with zipfile.ZipFile('files/input.zip', 'r') as zip_ref:
        zip_ref.extractall('files/input')  # Extraer en files/input

    # Procesar train y test
    for dataset in ['train', 'test']:
        data = []
        # La ruta base ahora es files/input/input/train o files/input/input/test
        base_path = os.path.join('files', 'input', 'input', dataset)
        
        for sentiment in ['negative', 'positive', 'neutral']:
            sentiment_dir = os.path.join(base_path, sentiment)
            
            # Verificar si el directorio de sentimiento existe
            if not os.path.exists(sentiment_dir):
                print(f"Warning: Directory '{sentiment_dir}' does not exist. Skipping.")
                continue  # Si no existe, continuar con el siguiente sentimiento

            # Procesar archivos de texto en el directorio de sentimiento
            for filename in os.listdir(sentiment_dir):
                if filename.endswith('.txt'):
                    file_path = os.path.join(sentiment_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                        if phrase:  # Solo agregar si la frase no está vacía
                            data.append({'phrase': phrase, 'target': sentiment})

        # Crear DataFrame y guardar
        if data:  # Solo guardar si hay datos
            df = pd.DataFrame(data)
            output_dir = 'files/output'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f'{dataset}_dataset.csv')
            df.to_csv(output_file, index=False)
        else:
            print(f"Warning: No data found for '{dataset}'. No CSV file created.")
print(pregunta_01())
   