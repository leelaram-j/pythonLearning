class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5

    def totalgetter(self):
        return self._total

    def totalsetter(self, t):
        if t < 0 or t > 500:
            print("Enter correct total")
        else:
            self._total = t


    total = property(totalgetter, totalsetter)

o = student(450)
print(o.total)
print(o.average())

o.total = 350
print(o.total)
print(o.average())