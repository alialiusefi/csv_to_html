from dataclasses import dataclass


@dataclass
class KeePassXCCSVRow:
    group: str
    title: str
    username: str
    password: str
    url: str
    notes: str
    totp: str
    icon: str
    last_modified: str
    created: str
