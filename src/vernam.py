from src.algorithm import Algorithm, File

class Vernam(Algorithm):
    def __init__(self, dim_max: int) -> None:
        super().__init__()
        self.dim_max = dim_max
    
    def __correct_key(self, key: str, length: int) -> str:
        return key * (length // len(key)) + key[:length%len(key)]
    
    def __int_key(self, key: str) -> int:
        return ord(key) % self.dim_max
    
    def encrypt(self, file: File, key: str) -> None:
        data = file.get_data()
        new_data_array = [0 for i in range(len(data))]
        key = self.__correct_key(key, len(data))
        for i, symbol in enumerate(data):
            new_data_array[i] = self.__int_key(key[i]) ^ symbol
        file.write_data(bytes(new_data_array))

    def decrypt(self, file: File, key: str) -> None:
        self.encrypt(file, key)
