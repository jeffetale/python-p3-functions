def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print("Hello, " + name + "!")
greet("John")

def greet_with_default(name = "John"):
    print("Hello, " + name + "!")
greet_with_default("Mercy")

def add(num1, num2):
    return num1 + num2
def total_sum():
    return add(10, 1)
print(total_sum())

def have(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
print(have(-16))