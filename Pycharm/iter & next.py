class student():
    def __iter__(self):
        self.no = 1
        return self
    def __next__(self):
        n = self.no
        self.no += 1
        return n
stu = student()

num = iter(stu)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))