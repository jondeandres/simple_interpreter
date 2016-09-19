from .token import Token


INTEGER, PLUS, EOF, SUBSTRACT = 'INTEGER', 'PLUS', 'EOF', 'SUBSTRACT'

OPS = {
    PLUS: lambda x, y: x + y,
    SUBSTRACT: lambda x, y: x - y
}


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    @property
    def current_char(self):
        if self.pos > len(self.text) - 1:
            return ''

        return self.text[self.pos]

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS, SUBSTRACT)

        right = self.current_token
        self.eat(INTEGER)

        return OPS[op.type](left.value, right.value)

    def eat(self, *token_types):
        if self.current_token.type not in token_types:
            self.error()

        self.current_token = self.get_next_token()

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        token = None

        self._skip_whitespaces()

        if self.current_char.isdigit():
            token = self._build_integer_token()
        elif self.current_char == '+':
            token = self._build_plus_token()
        elif self.current_char == '-':
            token = self._build_substract_token()

        if not token:
            return self.error()

        return token

    def _skip_whitespaces(self):
        while self.current_char == ' ':
            self.pos += 1

    def _build_integer_token(self):
        value = self.current_char
        self.pos += 1

        while self.current_char.isdigit():
            value += self.current_char

            self.pos += 1

        return Token(INTEGER, int(value))

    def _build_plus_token(self):
        token = Token(PLUS, self.current_char)
        self.pos += 1

        return token

    def _build_substract_token(self):
        token = Token(SUBSTRACT, self.current_char)
        self.pos += 1

        return token
