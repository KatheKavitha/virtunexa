def calculate(expression):
    try:
        result = eval(expression, {'__builtins__': {}})
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception:
        return "Error: Invalid input."