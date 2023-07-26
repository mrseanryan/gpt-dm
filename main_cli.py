from config__database_schema_creator import EXPERT_COMMANDS
import core

command_messages = core.create_command_messages(EXPERT_COMMANDS)
previous_messages = []

input_prompt = "How can I help you? (To exit, just press ENTER) >"
user_prompt = input(input_prompt)
while(user_prompt != None and len(user_prompt) > 0):
    print("---")
    print(f">> {user_prompt}")
    # should route to the right 'expert' chain!
    rsp = core.execute_prompt(user_prompt, previous_messages, command_messages)
    print(rsp)
    user_prompt = input(input_prompt)
