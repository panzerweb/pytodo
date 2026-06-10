from dataclasses import dataclass

@dataclass
class CommandDictionary:
    action: str
    description: str
    natural_lang: list[str]
