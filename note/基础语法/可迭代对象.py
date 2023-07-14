class Demo:
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.x:
            self.count += 1
            return self.count - 1
        else:
            raise StopIteration


# d = Demo(10)
# for x in d:
#     print(x)


class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


f = Fibonacci(12)
for x in f:
    print(x)
