from simple_interpreter.interpreter import Interpreter


def run():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue

        interpreter = Interpreter(text)
        print(interpreter.expr())
