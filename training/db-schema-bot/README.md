# db-schema-bot README

## Custom LLM via nanoGPT for a Database Schema

ML approach:

1. Create a small test dataset in CSV format, via Chat-GPT3.5 Turbo (why: power + cost)
2. Train a new LLM via nanoGPT (reserve 10% for test, 10% for cross-validation)
3. Human test
4. Repeat, with a large est dataset

### Test data format:

Description, Table (name), JSON

## Steps to train

See [song-writer-bot](../song-writer-bot/README.md) example.
