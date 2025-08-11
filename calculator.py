class Calculator:
    def add(self, x, y):
        result = x + y
        print(result)
    def double(self, x, y):
        result = x * 2
        print(result)

x = 3
y = 5
obj = Calculator()
obj.add(x, y)
obj.double(x, y)