import os
from typing import TextIO


class MyFileManager:
    def __init__(self, path: str, mode="r", encoding="UTF-8") -> None:
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self) -> TextIO:
        if os.path.exists(self.path):
            self.file = open(self.path, self.mode, encoding=self.encoding)
        else:
            self.file = open(self.path, "w", encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()

        if exc_type is IOError:
            return True
