from src.input import Input
from src.file import File
from src.caesar import Caesar
from src.vigenere import Vigenere
from src.vernam import Vernam

class Main:
    def __init__(self) -> None:
        self.program_input = Input()
        self.program_file = File(self.program_input.get_path())
        self.algo = self.program_input.get_algo()
        self.action = self.program_input.get_action()
        self.key = self.program_input.get_key()
        self.hackermode = self.program_input.get_hack()
    
    def start(self) -> None:
        if self.algo == 'caesar':
            algo = Caesar()
            if self.action == 'encrypt':
                algo.encrypt(self.program_file, self.key)
            elif not self.hackermode:
                algo.decrypt(self.program_file, self.key)
            else:
                algo.hack(self.program_file)
        
        if self.algo == 'vigenere':
            algo = Vigenere(self.program_file.get_max() + 1)
            if self.action == 'encrypt':
                algo.encrypt(self.program_file, self.key)
            else:
                algo.decrypt(self.program_file, self.key)
        
        if self.algo == 'vernam':
            algo = Vernam(self.program_file.get_max() + 1)
            if self.action == 'encrypt':
                algo.encrypt(self.program_file, self.key)
            else:
                algo.decrypt(self.program_file, self.key)


if __name__ == "__main__":
    program = Main()
    program.start()
    print('Done!')
