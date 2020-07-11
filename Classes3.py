class Math:
    def __init__(self, *args):
        self.args = args

    def Add(self):
        total = 0
        for i in self.args:
            total += i
        return total

    def Mul(self):
        total = 1
        for i in self.args:
            total *= i
        return total
    
    def Sub(self):
        total = 0
        for i in self.args:
            total -= i
        return total



if __name__ == "__main__":
    m1 = Math(2,5,6,8,6,8)
    print(m1.Add())