def setup():
    size(900,600)
def draw():
    RAZMER = 30
    cvet = 255
    for x in range(0,RAZMER*30,RAZMER)
        for y in range(0,RAZMER*30,RAZMER)
            fill(cvet)
            rect(x,y,RAZMER,RAZMER)
            if cvet == 255:
                cvet = 0
            else:
                cvet = 255
        if cvet == 255:
                cvet = 0
        else:
                cvet = 255
