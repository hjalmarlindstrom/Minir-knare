import math

def addition(x, y):
    print(x+y)
def subtraktion(x, y):
    print(x-y)
def multiplikation(x, y):
    print(x*y)
def division(x, y):
    print(x/y)
def addition3(x, y, z):
    print(x+y+z)
def subtraktion3(x, y, z):
    print(x-y-z)
def multiplikation3(x, y, z):
    print(x*y*z)
def division3(x, y, z):
    print(x/y/z)
def upphöjt(x, y):
    print(x**y)
def roten(a):
    print(math.sqrt(a))

while True:    
    print("Välj vad du vill göra")
    print("1.Addition")
    print("2.Subtraktion")
    print("3.Multiplikation")
    print("4.Division")
    print("5.Upphöjt")
    print("6. Roten")

    val = input("skriv räknesättet som du vill använda(1,2,3,4,5,6)")
    if val == "6":
        a = int(input("Skriv talet du vill ta roten ur"))
        if a < 0:
            print("Man kan inte ta kvadratroten ur ett negativt tal")
        else:
            roten(a)
    else:
        x = int(input("Skriv in det första talet"))
        y = int(input("Skriv in det andra talet"))
        if val == "1" or "2" or "3" or "4":
            tredje_tal = input("Vill du ha en tredje siffra? ")
            if tredje_tal == "ja" or tredje_tal == "Ja":
                z =int(input("Skriv in det tredje talet"))
                if val == "1":
                    addition3(x,y,z)
                elif val == "2":
                    subtraktion3(x,y,z)
                elif val == "3":
                    multiplikation3(x,y,z)
                elif val == "4":
                    if y or z == 0:
                        print("Det går inte!")
                    else:
                        division3
                        (x,y,z)
                elif val > "4":
                    print("Man kan inte använda tre tal i uphhöjt!")
            else:
                if val == "1":
                    addition(x,y)
                elif val == "2":
                    subtraktion(x,y)
                elif val == "3":
                    multiplikation(x,y)
                elif val == "4":
                    if y == 0:
                        print("Det går inte!")
                    else:
                        division(x,y)


    if val == "5":
        upphöjt(x, y)
   

  
    print("-----------------------")

