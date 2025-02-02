import sys
import os
import re
import numpy as np
from collections import Counter

def compute_statistics(file_path):
    """Calcula estadísticas básicas a partir de un archivo de números."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [float(line.strip().replace(',', '')) for line in file if re.match(r'^-?\d+(\.\d+)?$', line.strip())]
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    if not data:
        print("No se encontraron datos válidos en el archivo.")
        return

    n = len(data)
    mean = np.mean(data)
    median = np.median(data)
    mode = max(set(data), key=data.count) if data else None
    variance = np.var(data)
    std_dev = np.std(data)

    result = (f"Media: {mean}\nMediana: {median}\nModa: {mode}\n"
              f"Varianza: {variance}\nDesviación estándar: {std_dev}")
    print(result)
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as output:
        output.write(result)


def convert_numbers(file_path):
    """Convierte números a binario y hexadecimal."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [int(line.strip()) for line in file if re.match(r'^-?\d+$', line.strip())]
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    if not data:
        print("No se encontraron datos válidos en el archivo.")
        return
    
    results = [f"{num}: Binario {bin(num)[2:]}, Hex {hex(num)[2:].upper()}" for num in data]
    output_text = '\n'.join(results)
    print(output_text)
    with open('ConversionResults.txt', 'w', encoding='utf-8') as output:
        output.write(output_text)


def word_count(file_path):
    """Cuenta la frecuencia de palabras en un archivo de texto."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = re.findall(r'\b\w+\b', file.read().lower())
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    if not words:
        print("No se encontraron palabras en el archivo.")
        return
    
    word_counts = Counter(words)
    results = [f"{word}: {count}" for word, count in word_counts.items()]
    output_text = '\n'.join(results)
    print(output_text)
    with open('WordCountResults.txt', 'w', encoding='utf-8') as output:
        output.write(output_text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <tipo_de_operacion> <archivo>")
        sys.exit(1)
    
    operation = sys.argv[1]
    file_path = sys.argv[2]
    
    if not os.path.exists(file_path):
        print("El archivo no existe.")
        sys.exit(1)
    
    if operation == "statistics":
        compute_statistics(file_path)
    elif operation == "convert":
        convert_numbers(file_path)
    elif operation == "count":
        word_count(file_path)
    else:
        print("Operación no reconocida.")
        sys.exit(1)
