class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def Sub(self):
        return self.num1 - self.num2
    def Mul(self):
        return self.num1 * self.num2
    def Add(self):
        return self.num1 + self.num2
    


m = Math(8,3)
print(f'Addtion is : {m.Add()}')
print(f'Subtraction is : {m.Sub()}')
print(f'Multiplication is : {m.Mul()}')
