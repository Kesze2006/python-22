print("Amőba játék <3")

def palya():
    jatekter = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return jatekter

def babuk():
    x = input("Az első játékos mi szertne lenni X vagy O?")
    if x == "X":
        o == "O"
    else:
        x = "O"
    return (x,o)
