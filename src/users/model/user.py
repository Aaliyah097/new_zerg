class User:
    def __init__(self, telegram: str, telegram_id: int = None, is_active: bool = False):
        self.telegram = telegram
        self.telegram_id = telegram_id
        self.is_active = is_active

    def toggle_active(self):
        self.is_active = not self.is_active
