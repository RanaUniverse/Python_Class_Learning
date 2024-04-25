def double_add(x,y):
    result = 2*x + 2*y
    return f"The double of the sum is {result}"


class MathOperations:
    def add(self, x, y):
        result = x + y
        return f"The sum of {x} and {y} is {result}"

    def subtract(self, x, y):
        result = x - y
        return f"The difference between {x} and {y} is {result}"


class MathFunctions:
    def multiply(self, x, y):
        result = x * y
        return f"The product of {x} and {y} is {result}"

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        result = x / y
        return f"The division of {x} by {y} is {result}"

def main():
    math_op = MathOperations()
    math_func = MathFunctions()

    print(double_add(5,69))




if __name__ == "__main__":
    main()
