class Cake: 
    def __init__(self, p_color):
        self.color=p_color
    
    def change_color(self, new_color):
        self.color=new_color 
cake1= Cake("red")
cake2= Cake("green")  

print(cake1.color, cake2.color)
print('############')
cake2.change_color("Pink")
print(cake1.color, cake2.color)
