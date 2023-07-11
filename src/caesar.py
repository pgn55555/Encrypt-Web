from src.algorithm import Algorithm, File

class Caesar(Algorithm):
    def __init__(self) -> None:
        super().__init__()
    
    def encrypt(self, file: File, key: str) -> None:
        kLimitPower = file.get_max() + 1
        if kLimitPower == int(key):
            raise RuntimeWarning('Unsafety key')
        data = file.get_data()
        new_data_array = [0 for i in range(len(data))]
        key_int = int(key)
        for i, symbol in enumerate(data):
            new_data_array[i] = (symbol + key_int) % kLimitPower
        file.write_data(bytes(new_data_array))

    def decrypt(self, file: File, key: str) -> None:
        kLimitPower = file.get_max() + 1
        if kLimitPower == int(key):
            raise RuntimeWarning('Unsafety key')
        data = file.get_data()
        new_data_array = [0 for i in range(len(data))]
        key_int = int(key)
        for i, symbol in enumerate(data):
            new_data_array[i] = (symbol - key_int) % kLimitPower
        file.write_data(bytes(new_data_array))

    def hack(self, file: File) -> None:
        kLimitPower = file.get_max() + 1
        data = file.get_data()
        frequency = [0 for i in range(kLimitPower)]
        max_frequency = 0
        for symbol in data:
            frequency[symbol] += 1
            if frequency[symbol] > max_frequency:
                max_frequency = frequency[symbol]
                guess_key = symbol

        self.decrypt(file, guess_key)
