from sys import argv, getsizeof
from uuid import uuid4


class Exceptions:
    SYNTAX_ERROR = 'SYNTAX_ERROR'
    ARGUMENT_ERROR = 'ARGUMENT_ERROR'
    DIVISION_BY_ZERO = 'DIVISION_BY_ZERO'
    NULL_REGISTER = 'NULL_REGISTER'
    MOVE_ERROR = 'MOVE_ERROR'
    PUSH_ERROR = 'PUSH_ERROR'


class Commands:
    MOVE = 'MOVE'
    PUSH = 'PUSH'
    CREA = 'CREA'
    ADDI = 'ADDI'
    SUBI = 'SUBI'
    MULI = 'MULI'
    DIVI = 'DIVI'
    DEL = 'DEL'


class Compiler:
    def __init__(self, file):
        self.file = file
        self.exceptions = Exceptions()

    def load_file(self):
        file = open(self.file, 'r').readlines()
        for i in file:
            yield i

    def compile(self):
        pass

    def parse(self):
        for i in self.load_file():
            try:
                i = i.replace(' ', '')

            except Exception:
                raise Exception(self.exceptions.SYNTAX_ERROR)


class Environment:
    def __init__(self):
        self.registers = {}

    @property
    def registers_count(self):
        return len(self.registers)


class Operator:
    def __init__(self):
        self.exceptions = Exceptions()

    def MOVE(self, value, register):  # перемещает в пстой регистр
        if not register:
            register = value
        raise Exception(self.exceptions.MOVE_ERROR)

    def PUSH(self, value, register):
        register = value

    def CREA(self, register_name, memory):
        pass

    def ADDI(self, register_a, register_b, register_result):
        register_result = register_a + register_b

    def SUBI(self, register_a, register_b, register_result):
        register_result = register_a - register_b

    def MULI(self, register_a, register_b, register_result):
        register_result = register_a * register_b

    def DIVI(self, register_a, register_b, register_result):
        register_result = register_a / register_b

    def DEL(self, register):
        if not register:
            raise Exception(self.exceptions.NULL_REGISTER)
        del register


class SystemCall:
    def __init__(self, call_name, function):
        self.call_name = call_name
        self.function = function


class Register:
    def __init__(self, max_memory, key, _value):
        self.uid = uuid4()
        self.max_memory = max_memory
        self.key = key
        self._value = _value

    def set_value(self, value):
        if getsizeof(self.max_memory) < getsizeof(value):  # с помощью функции для определения занимаемой памяти
            raise Exception(f'Регистру {1} не хватает {self.uid} памяти.')  # передать аргументом экзепшн
        self._value = value

    def get_value(self):
        return self._value


c = Compiler(argv[-1])
c.parse()
