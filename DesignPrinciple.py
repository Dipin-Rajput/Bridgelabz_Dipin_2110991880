# Design Principles

# Design principles in Python are foundational guidelines that help developers create clean, maintainable, and efficient code. These principles align with Python's philosophy of simplicity and readability. Below are some key design principles and their explanations


# SOLID

# S: Single Responsibility Principle: A class should have only one reason to change, meaning it should have only one responsibility.

# Bad Example: A single class doing two tasks
class Calculator:
    def add(self, a, b):
        return a + b

    def print_result(self, result):
        print(f"Result: {result}")

# Good Example: Separate responsibilities into different classes
class Calculator:
    def add(self, a, b):
        return a + b

class Printer:
    def print_result(self, result):
        print(f"Result: {result}")

# Usage
calc = Calculator()
result = calc.add(2, 3)
Printer().print_result(result)


# O: Open/Closed Principle: Add new functionality by extending, not modifying, existing code.

# Bad Example: Modifying existing code for new operations
class Greeter:
    def greet(self, language):
        if language == "English":
            return "Hello"
        elif language == "Spanish":
            return "Hola"

# Good Example: Extend behavior using inheritance
class Greeter:
    def greet(self):
        pass

class EnglishGreeter(Greeter):
    def greet(self):
        return "Hello"

class SpanishGreeter(Greeter):
    def greet(self):
        return "Hola"

# Usage
greeters = [EnglishGreeter(), SpanishGreeter()]
for greeter in greeters:
    print(greeter.greet())


# L: Liskov Substitution Principle: A subclass should behave like its parent class.

# Bad Example: Subclass violates expected behavior
class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):
    def fly(self):
        return "I can't fly!"  # Violates the behavior of the parent class

# Good Example: Use base classes that correctly represent behavior
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "I can fly!"

class NonFlyingBird(Bird):
    def move(self):
        return "I can't fly, but I can walk."

# Usage
birds = [FlyingBird(), NonFlyingBird()]
for bird in birds:
    print(bird.move())


# I: Interface Segregation Principle: Don’t force a class to implement methods it doesn’t use.

# Bad Example: One interface with methods not needed by all classes
class Animal:
    def fly(self):
        pass

    def swim(self):
        pass

class Dog(Animal):
    def swim(self):
        return "Dog swims"
    def fly(self):
        pass  # Dog doesn't need this!

# Good Example: Use smaller, more specific interfaces
class Swimmable:
    def swim(self):
        pass

class Flyable:
    def fly(self):
        pass

class Dog(Swimmable):
    def swim(self):
        return "Dog swims"

class Bird(Flyable):
    def fly(self):
        return "Bird flies"


# D: Dependency Inversion Principle: Depend on abstractions, not concrete implementations.

# Bad Example: High-level class depends on a low-level class
class Lamp:
    def turn_on(self):
        return "Lamp is ON"

    def turn_off(self):
        return "Lamp is OFF"

class Switch:
    def __init__(self):
        self.lamp = Lamp()  # Switch depends directly on Lamp

    def operate(self, action):
        if action == "ON":
            return self.lamp.turn_on()
        elif action == "OFF":
            return self.lamp.turn_off()

# Usage
switch = Switch()
print(switch.operate("ON"))  # Output: Lamp is ON
print(switch.operate("OFF"))  # Output: Lamp is OFF

# Good Example: High-level class depends on an abstraction
# Abstract interface (abstraction)
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Low-level class: Lamp
class Lamp(Switchable):
    def turn_on(self):
        return "Lamp is ON"

    def turn_off(self):
        return "Lamp is OFF"

# Low-level class: Fan
class Fan(Switchable):
    def turn_on(self):
        return "Fan is ON"

    def turn_off(self):
        return "Fan is OFF"

# High-level class: Switch
class Switch:
    def __init__(self, device: Switchable):  # Depends on abstraction
        self.device = device

    def operate(self, action):
        if action == "ON":
            return self.device.turn_on()
        elif action == "OFF":
            return self.device.turn_off()

# Usage
lamp = Lamp()
fan = Fan()

lamp_switch = Switch(lamp)
fan_switch = Switch(fan)

print(lamp_switch.operate("ON"))  # Output: Lamp is ON
print(lamp_switch.operate("OFF"))  # Output: Lamp is OFF

print(fan_switch.operate("ON"))  # Output: Fan is ON
print(fan_switch.operate("OFF"))  # Output: Fan is OFF


# KISS (Keep It Simple, Stupid): Write code that is as simple as possible. Avoid overengineering or adding unnecessary complexity.


# DIY: Do it yourself

#  This is more of a mindset than a strict coding principle. It encourages developers to actively solve problems themselves, explore the codebase, and experiment with solutions instead of overly relying on others. It's about taking ownership and learning.


# DRY: Don't reapeat yourself: Avoid duplicating code or logic. If you see repeated patterns, abstract them into a reusable function, method, or module.

# Bad Example: Repeating the same logic
def calculate_area_rectangle(width, height):
    return width * height

def calculate_area_square(side):
    return side * side

# Good Example: Abstracting common logic
def calculate_area(shape, *dimensions):
    if shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "square":
        return dimensions[0] ** 2

# Usage
print(calculate_area("rectangle", 4, 5))  # Output: 20
print(calculate_area("square", 4))       # Output: 16


# YAGNI: You are'nt gonna need it: Don't add features or functionality until it is absolutely necessary. Premature optimization or overengineering often results in wasted effort.

# Bad Example: Adding unnecessary features
class User:
    def __init__(self, username):
        self.username = username
        self.age = None  # Premature feature: not used now
        self.address = None  # Premature feature: not used now

# Good Example: Only add what is needed
class User:
    def __init__(self, username):
        self.username = username

# Usage
user = User("Alice")
print(user.username)  # Only focus on the current need