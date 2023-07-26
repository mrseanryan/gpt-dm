from config__database_schema_creator import EXPERT_COMMANDS
import core

command_messages = core.create_command_messages(EXPERT_COMMANDS)
previous_messages = []

# TODO use is_debug to hide stuff
# TODO tell user the capabilities, at least at the start

initial_prompt = "What is the name of your application?"
user_prompt = input(initial_prompt)

input_prompt = "How can I help you? (To exit, just press ENTER) >"
while(user_prompt != None and len(user_prompt) > 0):
    print("---")
    print(f">> {user_prompt}")
    # should route to the right 'expert' chain!
    rsp = core.execute_prompt(user_prompt, previous_messages, command_messages)
    print(rsp)
    user_prompt = input(input_prompt)
