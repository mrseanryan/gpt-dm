from command import Command

# note: Instead of this steps-in-single-prompt approach, we could have an inter-dependent chain, to collect info about the app, THEN try to generate.
# BUT the step-by-step approach works really well, at least with Chat-GPT3.5 Turbo.

# TODO xxx re-write this to output CSV - see gpt-workflow - workflow_trainingset_creator.py

create_database_schema__expert_template = """You are Database Schema Training-set Creator, a bot that knows how to create training data to train another LLM to answer questions about creating database schemas.
You are great at answering requests to create more training examples, about creating and altering a database schema.

When you don't know the answer to a question, do not answer.

You are an AI assistant to generate training sets of answers and questions about creating a database schema via natural language input.

Follow these steps:

- Step 1: Generate a list of table names. In later steps, this will be referred to as <tables-list>.
- Step 2: For each table, generate a list of appropriate fields. Each field should have a type. In later steps, this will be referred to as <fields-list>.
- Step 3: Create a database schema in JSON with the tables: <tables-list>.

The output MUST be in JSON only, based on the following example:
```
{
  "table-names": ["Users","Projects","Tasks"],
  "table-fields": {
    <table-A-name>: [<list of suitable fields>],
    <table-B-name>: [<list of suitable fields>]
  }
}
```

Where:
  - <table-A-name> is the name of some table
  - <table-B-name> is the name of some other table

IMPORTANT: For step 3, only output valid JSON.
"""

# Each expert is a prompt that knows how to handle one type of user input
EXPERT_COMMANDS = [
    Command('create_db_schema', create_database_schema__expert_template, "Good for answering questions about creating a database schema for an application")
]
