class Student:
    def __init__(self, rno, marks):
        self.rno = rno
        self.marks = marks
    
    def Show(self):
        print(f"Marks of roll no {self.rno} is {self.marks}")
		
		
		
s1 = Student(22,97)
s1.Show()