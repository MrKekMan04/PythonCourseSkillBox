class MyDict(dict):
    def get(self, __key):
        result = super().get(__key)
        return result if result is not None else 0
