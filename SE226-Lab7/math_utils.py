def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print("Testing math_utils functions:")
    print("Add: ", add(3, 2))
    print("Subtract: ", subtract(3, 2))
    print("Multiply: ", multiply(3, 2))
    print("Divide: ", divide(3, 0))
    print("Power: ", power(2, 3))
    print("Mod: ", mod(5, 2))
