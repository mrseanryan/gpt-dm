from config__database_schema_creator import EXPERT_COMMANDS
import core

def test():
    command_messages = core.create_command_messages(EXPERT_COMMANDS)

    user_test_prompts = [
        "I want to set up my database",
        "My application is called Car-Parts-Inc. It needs to manage Cars, Wheels, windscreens and accessories.",
        "My application is called Euro-Shop. The shop sells household items which each have a price and unit volume.",
        # other prompts, that should NOT be handled by the Commands:
        "what is 2 + 5 divided by 10 ?",
        "Who won the battle of Agincourt, and why was it fought?",
        "What is my favourite color?",
        ]

    for user_prompt in user_test_prompts:
        previous_messages = []
        print("---")
        print(f">> {user_prompt}")
        # should route to the right 'expert' chain!
        rsp = core.execute_prompt(user_prompt, previous_messages, command_messages)
