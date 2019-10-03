
from .calculator import calculate
from .errors import CalculatorError

while True:
    try:
        user_input = input('Input - ')
    except (KeyboardInterrupt, EOFError):
        print(calculate(user_input))
        break
    except CalculatorError as e:
        print(e)
