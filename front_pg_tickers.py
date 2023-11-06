import pygame
import buttons


# ---------------------------
# tickers class defines the ticker box on the left of the main menu
# width, height and coords are defined here.
# main users parameters to print to screen
class tickers:
    def __init__(self):
        #I want a list of the tickers to be here
        self.btn = buttons.Button()
        self.msft = "7%"

        #parameters
        self.tabnWdth = 300
        self.tabHeit = 300
        self.tabX = 5  #(top left y coord of tab that will appear on scren)
        self.tabY = 300 #(top x ccord of tab that will apear)



        #I want the box outline to be here
    def boxOutline(self):
        tkrOutline = pygame.Rect(self.tabX,self.tabY,self.tabnWdth ,self.tabHeit )  # defines alt rect
        return tkrOutline
        # why use this? it's not a button. It's a pushable tab.
        #altBtn = pygame.Rect(self.btn.stk())  # defines alt rect
    def tkr_txt(self):
        font = pygame.font.SysFont('geneva', 16, bold='True')  # name size bold ital
        tkrTuple =(
        font.render('Whats popular', True, 'white'),
        font.render('Microsoft(MSFT)', True, 'white'),
        font.render('Alphabet(GOOGL)', True, 'white'))
        return tkrTuple
        #return font.render('Whats popular', True, 'white')  # defines alt txt




