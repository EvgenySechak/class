class Second:
     color = "red"
     form = "ferrari"
     def changecolor(self,newcolor):
          self.color = newcolor
     def changeform(self,newform):
          self.form = newform
 
obj1 = Second()
obj2 = Second()
 
print (obj1.color, obj1.form) # вывод на экран "red ferrari"
print (obj2.color, obj2.form) # вывод на экран "red ferrari
obj1.changecolor("green") # изменение цвета первого объекта
obj2.changecolor("blue")  # изменение цвет второго объекта
obj2.changeform("uaz")   # изменение машины
print('меняем цвет первой машины')
print (obj1.color, obj1.form) # вывод на экран "green circle"
print('меняем вторую машину и ее цвет')
print (obj2.color, obj2.form) # вывод на экран "blue uaz"
