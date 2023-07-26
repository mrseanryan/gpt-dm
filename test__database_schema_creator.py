from config__database_schema_creator import EXPERT_COMMANDS
import core

def test():
    command_messages = core.create_command_messages(EXPERT_COMMANDS)

    tests = [
        {
            "name": "General DB question",
            "prompts": [
                "I want to set up my database",
                "help me build my application"
            ]
        },
        {
            "name": "App creation - Car-Parts-Inc",
            "prompts": [
                "My application is called Car-Parts-Inc. It needs to manage Cars, Wheels, Tyres, windscreens and accessories.",
                "A car has four wheels and one windscreen and many accessories. A wheel has one tyre.",
                "Write the SQL to create the tables and populate with test data",
                "Create the test data in CSV format",
            ]
        },
        {
            "name": "App creation - Euro-Shop",
            "prompts": [
                "My application is called Euro-Shop. The shop sells household items which each have a price and unit volume.",
                "Show me how to create the database with some test data",
            ]
        },
        {
            "name": "Irrelevant prompts",
            "prompts": [
                # other prompts, that should NOT be handled by the Commands:
                "what is 2 + 5 divided by 10 ?",
                "Who won the battle of Agincourt, and why was it fought?",
                "What is my favourite color?",
           ]
        },
    ]

    for test in tests:
        previous_messages = []
        print(f"[[[TEST {test['name']}]]]")
        for user_prompt in test['prompts']:
            print("---")
            print(f">> {user_prompt}")
            # should route to the right 'expert' chain!
            rsp = core.execute_prompt(user_prompt, previous_messages, command_messages)
            print(rsp)
