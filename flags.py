import turtle  #importation de la turtle

#initiation de la tortue
tortue = turtle.Turtle()    
tortue.hideturtle()
tortue.speed(0)


#definition des fonctions de dessin

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    
    Args:
        size (float): La taille du côté du carré.
        color (str): La couleur du carré.
    """
    
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, color):
    """Trace un rectangle plein de largeur `width`, de hauteur `height` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un coin du rectangle et orientée en direction
         de la longueur du rectangle.
    post: Le rectangle a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur du rectangle.
        height (float): La hauteur du rectangle.
        color (str): La couleur du rectangle.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def belgian_flag(width):
    """Dessine un drapeau belge avec les couleurs noire, jaune et rouge.

    pre: La tortue `tortue` est initialisée.
         La position de départ (`start_x`, `start_y`) est définie.
    post: Le drapeau belge est dessiné avec les proportions correctes.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur totale du drapeau belge.
    """
    size_x = width/3
    size_y = size_x*2

    global start_x
    global start_y

    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, "black")
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, "yellow")
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, "red")

def three_color_flag(width, color1, color2, color3):
    """Dessine un drapeau à trois bandes horizontales de couleurs spécifiées.

    pre: La tortue `tortue` est initialisée.
         La position de départ (`start_x`, `start_y`) est définie.
    post: Le drapeau à trois bandes est dessiné avec les proportions correctes.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur totale du drapeau.
        color1 (str): La couleur de la première bande.
        color2 (str): La couleur de la deuxième bande.
        color3 (str): La couleur de la troisième bande.
    """
    size_x = width/3
    size_y = size_x*2

    global start_x
    global start_y

    end_flag_x = start_x + width
    end_flag_y = start_y

    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, color1)
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, color2)
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_x += size_x
    rectangle(size_x, size_y, color3)

    start_x = end_flag_x
    start_y = end_flag_y

def three_color_flag_horizontal(width, color1, color2, color3):
    """Dessine un drapeau à trois bandes horizontales de couleurs spécifiées.

    pre: La tortue `tortue` est initialisée.
         La position de départ (`start_x`, `start_y`) est définie.
    post: Le drapeau à trois bandes horizontales est dessiné avec les proportions correctes.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur totale du drapeau.
        color1 (str): La couleur de la première bande.
        color2 (str): La couleur de la deuxième bande.
        color3 (str): La couleur de la troisième bande.
    """
    size_x = width
    size_y = size_x*2/9

    global start_x
    global start_y

    end_flag_x = start_x + width
    end_flag_y = start_y

    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_y -= size_y
    rectangle(size_x, size_y, color1)
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_y -= size_y
    rectangle(size_x, size_y, color2)
    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()
    start_y -= size_y
    rectangle(size_x, size_y, color3)

    start_x = end_flag_x
    start_y = end_flag_y

def european_flag(width, color):
    """Dessine le drapeau de l'Union Européenne.

    pre: La tortue `tortue` est initialisée.
         La position de départ (`start_x`, `start_y`) est définie.
    post: Le drapeau de l'Union Européenne est dessiné avec les proportions correctes.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur totale du drapeau.
        color (str): La couleur de fond du drapeau.
    """
    size_x = width
    size_y = width*2/3

    tortue.penup()
    tortue.goto(start_x, start_y)
    tortue.pendown()

    tortue.color("darkblue")
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(size_x)
        tortue.right(90)
        tortue.forward(size_y)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

    star_radius = size_y / 12
    center_x = start_x + size_x / 2 - star_radius/2
    center_y = start_y - size_y / 2 

    stars(star_radius, center_x, center_y, "yellow")

def stars(size, x, y, color):
    """Dessine des étoiles sur le drapeau de l'Union Européenne.

    pre: La tortue `tortue` est initialisée.
         La position (`x`, `y`) est définie.
         `size` spécifie la taille des étoiles.
    post: Les étoiles sont dessinées sur le drapeau de l'Union Européenne.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        size (float): La taille des étoiles.
        x (float): La coordonnée x du centre des étoiles.
        y (float): La coordonnée y du centre des étoiles.
        color (str): La couleur des étoiles.
    """

    circle = size * 12 / 2 - size*2

    number_stars = 12
    tortue.color(color)
    tortue.penup()
    for i in range(number_stars):
        tortue.goto(x, y)
        tortue.setheading(90)
        tortue.right(360/number_stars*i)
        tortue.forward(circle)
        tortue.begin_fill()
        tortue.setheading(0)
        for i in range(5):
            tortue.forward(size)
            tortue.right(144)
        tortue.end_fill()

def grece(width):
    """Dessine le drapeau de la Grèce.

    pre: La tortue `tortue` est initialisée.
         La position de départ (`start_x`, `start_y`) est définie.
    post: Le drapeau de la Grèce est dessiné avec les proportions correctes.
          La tortue est à la même position et orientation qu'au départ.

    Args:
        width (float): La largeur totale du drapeau.
    """

    size_x = width
    size_y = size_x*2/27

    global start_x
    global start_y

    end_flag_x = start_x + width
    end_flag_y = start_y

    start_flag_x = start_x
    start_flag_y = start_y

    for i in range(9):
        tortue.penup()
        tortue.goto(start_x, start_y)
        tortue.pendown()

        if i % 2 == 0:
            rectangle(size_x, size_y, "blue")

        else:
            rectangle(size_x, size_y, "white")

        start_y = start_y - size_y    

    start_x = start_flag_x
    start_y = start_flag_y

    tortue.goto(start_x, start_y)

    square_x = (size_x / 3 - size_y) / 2

    square(size_x / 3, "white")

    tortue.goto(start_x, start_y)

    square(square_x, "blue")
    tortue.goto(start_x + square_x + size_y, start_y)
    square(square_x, "blue")
    tortue.goto(start_x + square_x + size_y, start_y - square_x - size_y)
    square(square_x, "blue")
    tortue.goto(start_x, start_y - square_x - size_y)
    square(square_x, "blue")

    start_x = end_flag_x
    start_y = end_flag_y


#debut de l'utilisation des fonctions de dessin

#modification de la position
start_x = -100
start_y = 0

european_flag(400) #dessin drapeau européen

start_x = -450
start_y = 200

grece(100) #dessin drapeau grece

start_x += 100

belgian_flag(100) #dessin drapeau belgique

start_x += 100

three_color_flag(100,"blue","white","red") #dessin drapeau france

start_x += 100

three_color_flag(100,"green","white","red") #desisn drapeau italie

start_x += 100

three_color_flag_horizontal(100,"black","red","yellow") #dessin drapeau allemagne

start_x += 100

three_color_flag_horizontal(100,"blue","white","red") #dessin drapeau pays-bas


turtle.exitonclick() #quitte au click

