class File():
    def __init__(self, path: str) -> None:
        self.path = path
        with open(self.path, 'rb') as file:
            self.data = file.read()
        with open(self.path, 'rb') as file:
            self.max_byte = max(file.read())
    
    def get_data(self) -> str:
        return self.data
    
    def get_max(self) -> int:
        return self.max_byte
    
    def write_data(self, data: str) -> None:
        with open(self.path, 'wb') as file:
            self.data = file.write(data)
