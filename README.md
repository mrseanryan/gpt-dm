# gpt-dm
Data modelling via natural language using an LLM. Outputs JSON or SQL. Also generates Test data.

## Design

Loosely based on [gpt-command](https://github.com/mrseanryan/gpt-command), using a sequence of 'expert' chains.
Each chain is an expert on one task, for example, creating JSON of a database schema, or generating test data in CSV format.

## Dependencies

Requires a LLM - by default, uses OpenAI's ChatGPT.

## Usage

To use as a CLI (Command Line Interface) REPL (Read-Eval-Print Loop) prompt:
```go.sh```

or to use as a web server:

```go_web.sh```

For the web server, you need to pass the user prompt as GET query parameter 'p'.

Example:

- http://localhost:8083/?p=I%20need%20a%20new%20letter

So, another application can use the web server to send in natural language prompts from the user, and receive response in appropriate format (JSON or CSV or SQL).

The other application can then act on the given output.

## Commands

Commands with prompts are configured to suit your application.

Example - see [config__application_commander.py](config__application_commander.py).

### Example Output

xxx

# Non-Command user prompts

User prompts that are not related to any of the known Commands, are sent directly to the LLM.

Examples:

```
>> Who won the battle of Agincourt, and why was it fought?
{"general_response": " The battle of Agincourt was fought in 1415 during the Hundred Years' War between the English and French. The English army, led by King Henry V, was victorious in the battle. The French army was significantly larger, but the English were able to win thanks to their superior tactics. "}
```

```
>> What is my favourite color?
{"general_response": " I'm sorry, I don't know. "}
```

## Set up

```
pip3 install --upgrade openai
```

Set environment variable with your OpenAI key:

```
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)

Load in current terminal:

```
source ~/.zprofile
```

## Test

`test.sh`

or

`python3 test.py`
