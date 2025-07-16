from dataclasses import dataclass

@dataclass
class Prototype:
    prototype_id: int
    prototype_name: str
    model: str
    user_id: int