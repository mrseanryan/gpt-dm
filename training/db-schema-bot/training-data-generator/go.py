import os
import sys

from database_schema_trainingset_creator import EXPERT_COMMANDS
import core

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} <path to output file JSON>")

json_file_path = sys.argv[1]

command_messages = core.create_command_messages(EXPERT_COMMANDS)

# TODO xxx how to make more random? up temperature could risk the format...
user_prompt = "Create training data with 10 tables"

previous_messages = []
print("---")
print(f">> {user_prompt}")
rsp = core.execute_prompt(user_prompt, previous_messages, command_messages)
print(rsp)

LLM_LINE_SEP = '\n'

def remove_header_line(rsp):
    lines = rsp.split(LLM_LINE_SEP)
    return LLM_LINE_SEP.join(lines[1:])

json_file_path_no_extension = os.path.splitext(json_file_path)[0]

def next_file_path(json_file_path_no_extension, file_id):
    return f"{json_file_path_no_extension}_{file_id}.json"

file_id = 1
json_file_path_with_id = next_file_path(json_file_path_no_extension, file_id)
while os.path.isfile(json_file_path_with_id):
    file_id += 1
    json_file_path_with_id = next_file_path(json_file_path_no_extension, file_id)

def write_out(rsp, json_file_path):
    file_mode = 'w'
    print(f"  Writing to {json_file_path}")
    with open(json_file_path, file_mode, encoding='utf-8') as f:
        f.write(rsp + LLM_LINE_SEP)

write_out(rsp, json_file_path_with_id)
