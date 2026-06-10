from pytodo.utils.commands import COMMANDS

def parse_command(text: str) -> str | None:
    text = text.lower().strip()

    for command in COMMANDS:
        for keyword in command.natural_lang:
            if keyword in text:
                return command.action

    return None