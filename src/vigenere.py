from src.algorithm import Algorithm, File

class Vigenere(Algorithm):
    def __init__(self, dim_matrix: int) -> None:
        super().__init__()

        self.dim_matrix = dim_matrix
        self.code_matrix = []
        for i in range(dim_matrix):
            self.code_matrix.append([])
            for j in range(dim_matrix):
                self.code_matrix[i].append((i + j) % dim_matrix)
    
    def __int_key(self, key: str) -> int:
        return ord(key) % self.dim_matrix
    
    def encrypt(self, file: File, key: str) -> None:
        data = file.get_data()
        new_data_array = [0 for i in range(len(data))]
        for i, symbol in enumerate(data):
            new_data_array[i] = self.code_matrix[self.__int_key(key[i % len(key)])][symbol]
        file.write_data(bytes(new_data_array))

    def decrypt(self, file: File, key: str) -> None:
        data = file.get_data()
        new_data_array = [0 for i in range(len(data))]
        for i, symbol in enumerate(data):
            new_data_array[i] = self.code_matrix[0][symbol - self.__int_key(key[i % len(key)])]
        file.write_data(bytes(new_data_array))
