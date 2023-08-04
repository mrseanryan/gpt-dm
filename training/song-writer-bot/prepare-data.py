import os
import sys
import tiktoken
import numpy as np
import pandas as pd

if len(sys.argv) != 3:
    print(f"USAGE: {sys.argv[0]} <path to data CSV file> <project name>")
    exit(666)

path_to_data_csv_file = sys.argv[1]
project_name = sys.argv[2]

df = pd.read_csv(path_to_data_csv_file)
data = df['text'].str.cat(sep='\n')

n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'data', project_name, 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'data', project_name, 'val.bin'))
