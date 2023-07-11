from src.file import File

class Algorithm:
    def __init__(self) -> None:
        pass

    def encrypt(self, file: File, key: str) -> None:
        raise NotImplementedError('Incorrect function called') 

    def decrypt(self, file: File, key: str) -> None:
        raise NotImplementedError('Incorrect function called') 
