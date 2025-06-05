from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    full_name: str
    email: str
    photo_path: str
    department: str  # Örnek: Üretim, Depo, Ofis
