import json
from states.user_state import UserState


class MyDataBase:

    def __init__(self, path: str):
        self.path = path

    def load(self) -> dict:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save(self, db) -> None:
        with open(self.path, mode='w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=4)

    def update(self, user: UserState) -> None:
        db = self.load()
        user_dict = user.user_to_dict()
        user_id = str(user_dict['user_id'])
        db[user_id] = user_dict
        self.save(db)

    def get_user(self, user_id: int) -> UserState | None:
        db = self.load()
        user_dict = db[str(user_id)]
        return UserState.user_to_obj(user_dict) if user_dict else None
