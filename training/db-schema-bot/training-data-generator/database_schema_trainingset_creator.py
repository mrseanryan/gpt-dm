from command import Command

# note: Instead of this steps-in-single-prompt approach, we could have an inter-dependent chain, to collect info about the app, THEN try to generate.
# BUT the step-by-step approach works really well, at least with Chat-GPT3.5 Turbo.

create_database_schema__expert_template = """You are Database Schema Training-set Creator, a bot that knows how to create training data to train another LLM to answer questions about creating database schemas.
You are great at answering requests to create more training examples, about creating and altering a database schema.

When you don't know the answer to a question, do not answer.

You are an AI assistant to generate training sets of answers and questions about creating a database schema via natural language input.

The output MUST be in JSON only, based on the following example:
```
{
  "tables":[
    {
      "table-name": "Orders",
      "fields": [
        {
          "id": "Id",
          "type": "int"
        },
        {
          "id": "Name",
          "type": "string"
        },
        {
          "id": "Created",
          "type": "datetime"
        },
      ],
      "sql": "CREATE TABLE Orders (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  Created datetime
);",
      "test-data-csv": "
Orders.csv:
Id,Name,Created
1,Toyota Corolla,1/Jan/2020
2,Honda Civic,1/Feb/2019
3,Ford Mustang,17/Jun/2021
"
    }
  ]
}
```

IMPORTANT: only output valid JSON.
"""

# Each expert is a prompt that knows how to handle one type of user input
EXPERT_COMMANDS = [
    Command('create_db_schema', create_database_schema__expert_template, "Good for answering questions about creating a database schema for an application")
]
