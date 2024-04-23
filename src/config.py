from os import path
from random import randint

class Algo:
    algos = ['caesar', 'vernam', 'vigenere']

    def __init__(self, algo: str) -> None:
        if algo not in self.algos:
            raise AttributeError('Incorrect name of algorithm')
        self.mode_algo = algo
    
    def get_name(self) -> str:
        return self.mode_algo

class Action:
    actions = ['encrypt', 'decrypt']

    def __init__(self, action: str) -> None:
        if action not in self.actions:
            raise AttributeError('Incorrect name of action')
        self.mode_action = action
    
    def get_name(self) -> str:
        return self.mode_action

class Config:
    def __get_length_file(self) -> int:
        with open(self.get_path(), 'rb') as file:
            length = len(file.read())
        return length

    def __genetate_key(self, algo: str) -> str:
        if algo == 'caesar':
            return str(randint(1, 20))
        
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        length = self.__get_length_file()
        length = 10 if length >= 10 else length
        key = [alphabet[randint(0, len(alphabet) - 1)] for i in range(length)]
        return ''.join(key)


    def __parse_and_validation(self) -> None:
        if len(self.raw_data) != 4:
            raise AttributeError('Need 4 arguments')

        self.parse_data = dict(key='-1', hackermode=False)

        if not path.exists(self.raw_data[0]):
            raise AttributeError('Path does not exists')
        self.parse_data['path'] = path.abspath(self.raw_data[0])
        self.parse_data['algo'] = Algo(self.raw_data[1])
        self.parse_data['action'] = Action(self.raw_data[2])

        if self.raw_data[3] != 'hackermode':
            if self.raw_data[3] == 'generate':
                if self.raw_data[2] == 'decrypt':
                    raise AttributeError('Cannot generate key when you decrypt')
                self.raw_data[3] = self.__genetate_key(\
                    self.parse_data['algo'].get_name())
            
            self.parse_data['key'] = self.raw_data[3]
            return

        if not (self.raw_data[3] == 'hackermode' and self.raw_data[1] == 'caesar'\
                and self.raw_data[2] == 'decrypt'):
            raise AttributeError('You are not hacker')
        self.parse_data['hackermode'] = True

    def __init__(self, raw_data: list) -> None:
        self.raw_data = raw_data
        self.__parse_and_validation()
    
    def get_path(self) -> str:
        return self.parse_data['path']

    def get_algo(self) -> str:
        return self.parse_data['algo'].get_name()
    
    def get_key(self) -> str:
        return self.parse_data['key']
    
    def get_action(self) -> str:
        return self.parse_data['action'].get_name()
    
    def get_hack(self) -> str:
        return self.parse_data['hackermode']
