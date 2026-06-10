def parse_command(text: str) -> str | None:
    text = text.lower()

    command_keywords = {
        "add": [
            "add",
            "create",
            "new",
            "insert"
        ],

        "update": [
            "update",
            "edit",
            "modify"
        ],

        "read": [
            "read",
            "show",
            "list",
            "display",
            "view"
        ],

        "delete": [
            "delete",
            "remove",
            "erase"
        ],

        "toggle": [
            "toggle",
            "complete",
            "incomplete",
            "finish"
        ],

        "bulk_add": [
            "bulk",
            "multiple"
        ],

        "search_date": [
            "search",
            "find date"
        ],

        "days_ago": [
            "yesterday",
            "days ago"
        ],

        "stats": [
            "stats",
            "statistics"
        ],

        "help": [
            "help",
            "commands"
        ],

        "quit": [
            "quit",
            "exit",
            "close"
        ]
    }

    for command, keywords in command_keywords.items():
        for keyword in keywords:
            if keyword in text:
                return command

    return None