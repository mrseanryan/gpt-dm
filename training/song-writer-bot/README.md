# song-writer-bot README

## Custom LLM via nanoGPT for a Song Writer bot

Based on https://github.com/karpathy/nanoGPT

Following directions in https://sophiamyang.medium.com/train-your-own-language-model-with-nanogpt-83d86f26705e

### Setup

```
pip3 install torch numpy transformers datasets tiktoken wandb tqdm pandas
```

1. Get data set
https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

2. Use bash to extract smaller set (at least for 1st training attempt)

```
head -100000 spotify_millsongdata.csv > spotify_millsongdata.first100k.csv
```

3. Edit the file, deleting the last half-song.

4. Prepare the data (tokenise it)

```
python prepare-data.py ~/Downloads/ML-kaggle/spotify_millsongdata.first100k.csv song-writer
```

Output is like:

```
  train has 914,242 tokens
  val has 103,989 tokens
```

5. Train using the training set part of the data

```
./train.sh
```

6. Test it out!

```
./test.sh
```
