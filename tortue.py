import turtle

# def escalier(taille, nb):
#     for i in range(0, nb):
#         t.forward(taille)
#         t.left(90)
#         t.forward(taille)
#         t.right(90)
#     t.forward(30)
#
# t = turtle.Turtle()
# escalier(10,10)

# turtle.done()

def carre(taille):
          for i in range(0, 4):
              t.forward(taille)
              t.right(90)

def carres(taille_depart, nb):
    for i in range (0, nb):
        taille = (i+1)*taille_depart
        carre(taille)

t = turtle.Turtle()
carres(20, 10)

turtle.done()