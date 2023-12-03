print("WELCOME TO DA CALCULATOR!")
function2 = ""
def minus(a,b):
    
    return a-b
def add (a,b):
    
    return a+b
def times (a,b):
    return a*b
def divide(a,b):
    return a/b
import numpy as np

yes = "yes"

while yes == "yes":
    function1 = str(input("Normal or trigonometry or geometry?")).lower()
    if function1 == "normal":
        function2 = input("Minus,add,multiply or divide?").lower()
    
        num1 = int(input("please first number"))
        num2 = int(input("please second number"))
    
        if function2 == "minus":
        
            print(minus(num1,num2))
        if function2 == "add":
        
            print(add(num1,num2))
        if function2 == "multiply":
            print(times(num1,num2))
        if function2 == "divide":
            print(divide(num1,num2))
    elif function1 == "trigonometry":
        function2 = input("sin,tan or cos?").lower()
        if function2 == "sin":
            x = int(input("degrees"))
            print(np.sin(np.deg2rad(x)))
        if function2 == "tan":
            x = int(input("degrees"))
            print(np.tan(np.deg2rad(x)))
        if function2 == "cos":
            x = int(input("degrees"))
            print(np.cos(np.deg2rad(x)))
    elif function1 == "geometry":
        function2 = input("3D or 2D")
        if function2 == "3D":
            function3 = input("ok what shape? cube or prism or sphere or pyramid  ")
            if function3 == "cube":
                sidelength = int(input("the side length please"))
                print("the cube is around" , sidelength*sidelength*sidelength , "cm^3")
            if function3 == "prism":
                basearea = int(input("the base please"))
                height = int(input("height please"))
                print("the prism is around" , basearea*height , "cm^3")
            if function3 == "pyramid":
                base = int(input("the base please"))
                height = int(input("the height please"))
                print("the pyramid is around" , sidelength*height/3 , "cm^3")
            if function3 == "sphere":
                radius = int(input("radius please"))
                print("the sphere is around" , 4/3*radius*radius*radius*22/7 , "cm^3")
        elif function2 == "2D":
            function3 = input("square triangle rectangle parallelogram or a circle?")
            if function3 == "square":
                sidelength = int(input("the side length please"))
                print("the square is around" , sidelength*sidelength , "cm^2")
            if function3 == "triangle":
                sidelength = int(input("the side length please"))
                height = int(input("height please"))
                print("the square is around" , sidelength*height/2 , "cm^2")
            if function3 == "rectangle":
                height = int(input("height please"))
                width = int(input("the width please"))
                print("the rectangle  is around" , width*height , "cm^2")
            if function3 == "parallelogram":
                height = int(input("height please"))
                width = int(input("the width please"))
                print("the parallelogram is around" , width*height , "cm^2")
            if function3 == "circle":
                radius = int(input("radius please"))
            
                print("the radius is around" , radius*radius*22/7 , "cm^2")
    else:
        print("i cant read your mind or read your language please use the options provided thanks")
    yes = input("yes or no calculate again?")
print("thank you for using this calculator!")
