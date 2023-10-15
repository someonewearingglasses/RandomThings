class LineEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}"
    
    def standard_form(self):
        return f"{self.a}x + {self.b}y = {-1 * self.c}"
    def general_form(self):
        return f"{self.a}x + {self.b}y {self.c} = 0"

class FormSI:
    def __init__(self, m, b):
        self.m = m
        self.b = b
        
    def __str__(self):
        return f"y = {self.m}x + {self.b}"
    
    def remove_mdenom(self):
        self.current = ""
        for x in self.m: 
            if x == "/":
                self.current = ""
            if x == "x":
                break
            self.current += x
        try:
            denominator = int(self.current[1:])
            self.b = denominator * self.b
            numerator = ""
            for m1 in self.m:
                if m1 != "/":
                    numerator += m1
                else:
                    break
            self.m = int(numerator)
            return f"{denominator}(y = {self.m}/{denominator}x + {self.b//denominator}) --> {denominator}y = {self.m}x + {self.b}"
        except:
            pass
        return f"y = {self.m}x + {self.b}"
    
    def distribution(self):
        if self.current:
            #assign fstrings to variables to make conditions for terms
            previous = ""
            step2 = ""
            simplified = ""
            return f"{self.current[1:]}y = {self.m}x + {self.b} --> {self.m * -1}x + {self.current[1:]}y + {self.b} = 0 --> {self.m}x - {self.current[1:]}y - {self.b} = 0"
        return f"y = {self.m}x + {self.b} --> {self.m * -1}x + y + {self.b} = 0 --> {self.m}x - y - {self.b} = 0"
class FormPS:
    def __init__(self, m, x, y):
        pass
    
class Form2P:
    def __init__(self, x1, y1, x2, y2):
        pass
if __name__ == '__main__':
    print("")
    print("What form was given? [1]Slope-Intercept [2]Point-Slope [3]Two-Point")
    choice = int(input("Type here: "))
    if choice == 1:
        m = input("m = ")
        b = int(input("b = "))
        mb = FormSI(m,b)
        print(f"{mb} --> {mb.remove_mdenom()}")
        print(mb.distribution())
    print(" ")
