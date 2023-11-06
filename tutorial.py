import pygame
# ---------------------------

class Tutorial:

    def __init__(self):
        self.boxX = 500
        self.boxY = 700
        self.boxWdth = 300
        self.boxHight = 300
        self.tutBox1 = "Hello, this is about a 1 minute tutorial. "
        self.cont = "Yes"
        self.quit = "No"
        #self.tutTxt = pygame.font.render('Search stocks', True, 'white')  # defines start text

    def displayTut(self):
        #return self.boxX, self.boxY, self.boxWdth, self.boxHight
        tutBox= pygame.Rect(self.boxX, self.boxY, self.boxWdth, self.boxHight  )  # defines start rect
        return tutBox