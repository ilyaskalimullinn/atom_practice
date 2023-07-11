from typing import List

from cantools.database import load_file


class CanDataJ1939ReaderService:
    def decode_data(self, dbc_path: str, data_path: str) -> List:
        can_db = load_file(dbc_path)
        with open(data_path, "rb") as f:
            raw_data = f.read()
        results = []
        for message in can_db.messages:
            results.append(message.decode(raw_data))

        return results
