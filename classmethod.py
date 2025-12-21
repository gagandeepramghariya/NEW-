class student:
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
    
    @classmethod
    def using_cls_method(cls,file_path):
        f=open(file_path,'r')
        student_data=f.read()
        name, gender, age=student_data.split( ) 
        f.close()
        obj=cls(name, gender, age)
        return obj
           

 
 
print("-----------")
s2 = student.using_cls_method('student.txt')
s2.display()
