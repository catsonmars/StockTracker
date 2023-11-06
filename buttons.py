#---------------------------
# Button class defines button parameters such as width and location
# main uses class to define and print buttons to screen.


class Button:


    def __init__(self):
        #general
        self.butnWdth = 150
        self.butnHeit = 50

        #start buttons
        self.butnX = 100
        self.butnY = 100

        #alt buttons
        self.altbutnX = 350
        self.altbutnY = 100

        #stocks
        self.stkbutnX = 600
        self.stkbutnY = 100

        #add button(square in circle)
        self.radius = 20
        self.centerX = 270
        self.centerY = 570


    def start_btn(self): #parameters for drawing rect
        btnParams = (self.butnX, self.butnY, self.butnWdth, self.butnHeit)
        return btnParams

    def news(self): #parameters for drawing rect
        return (self.altbutnX, self.altbutnY, self.butnWdth, self.butnHeit)

    def Trending(self): #parameters for drawing rect
        return (self.stkbutnX, self.stkbutnY, self.butnWdth, self.butnHeit)

    def add(self): #circle(surface, color, center, radius) -> Rect
        return (self.centerX ,self.centerY)

    #define normal button color
    def butn_color(self):
        return (197, 197, 197) #(127, 127, 127)
    #define button color when curson is floating above button
    def butn_hvr_color(self):
        return (17, 47, 227)


    def alt(self):
        return (self.altbutnX, self.altbutnY, self.butnWdth, self.butnHeit)

