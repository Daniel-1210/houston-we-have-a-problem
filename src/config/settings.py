thonimport json
from pathlib import Path

class Settings:
    @staticmethod
    def load():
        """
        Loads settings from settings.example.json.
        A real app would use settings.json, but this remains a safe template.
        """
        file_path = Path(__file__).parent / "settings.example.json"
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)