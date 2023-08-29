# db-schema-bot README

## Custom LLM via nanoGPT for a Database Schema

ML approach:

1. Create a small test dataset in CSV format, via Chat-GPT3.5 Turbo (why: power + speed + low effort)
2. Train a new LLM via nanoGPT (reserve 10% for test, 10% for cross-validation)
3. Human test
4. Repeat, with a large test dataset

### Test data format:

Description, Table (name), JSON

## Training

See [README](training/README.md)
