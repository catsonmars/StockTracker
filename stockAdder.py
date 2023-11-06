import pygame
import Yahoo_Finance_Stock_Ticker as yah
import yfinance as yf
# ---------------------------

class stock_adder:

    def __init__(self):
        self.stk_screen = pygame.display.set_mode((1120, 880))
        # parameters of search box(and txt)
        self.srchX = 300
        self.srchY = 100
        self.srchWdth = 175
        self.srchHite = 35
        self.srchCntent = ''
        self.txtEnter = False
        self.font = pygame.font.SysFont('geneva', 12, bold='True')  # name size bold ital
        self.srchRect = pygame.Rect(self.srchX, self.srchY, self.srchWdth, self.srchHite)  # defines stk rect
        self.srchTxt = self.font.render(self.srchCntent, True, 'red')  # defines stock text
        self.prices = {}
        self.running = False
        self.quotes = []
        #self.tkr_aftr_entr =''




    def runPage(self):
        running = True
        x = 100
        y = 500
        width = 150
        height = 35

        tkr_aftr_entr = '' #used to query the stock

        srchCntent = ''
        txtEnter = False
        begnQuery = False

        font = pygame.font.SysFont('geneva', 18, bold='True')  # name size bold ital
        srchRect = pygame.Rect(x, y, width, height)  # defines stk rect
        srchTxt = font.render(srchCntent, True, 'red')  # defines stock text
        #self.stk_screen
        while running:
            self.stk_screen.fill((255, 242, 255))  # 133,112,218

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                rct = pygame.draw.rect(self.stk_screen, 'black', (srchRect), 3)  # create search rect object
                #srchRect = pygame.Rect(x, y, width, height)  # defines stk rect
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if srchRect.collidepoint(event.pos):
                       pass
                    # WANT to enter text
                if event.type == pygame.KEYDOWN:
                    print("key down")
                    # translate what user wrote into font.render
                    srchCntent += event.unicode
                    print(srchCntent)
                    if event.key == pygame.K_BACKSPACE:
                        print("removing a bit")
                        srchCntent = srchCntent[:-2] #this hasss to be -2
                        print(": ", srchCntent)
                    if event.key == pygame.K_RETURN:
                        tkr_aftr_entr = srchCntent
                        print("user has entered ", tkr_aftr_entr)
                        begnQuery = True
                        #self.tickers(tkr_aftr_entr) When here it calls yfinance func way too much
                self.stk_screen.blit(srchTxt, (x, y))
                srchTxt = font.render(srchCntent, True, 'black')  # defines stock text

                begnQuery = self.tickers(tkr_aftr_entr,begnQuery) #when here triggers contatination error
                pygame.display.flip()


        self.stk_screen.blit(self.srchTxt, (self.srchX, self.srchY))
        srchTxt = self.font.render(self.srchCntent, True, 'black')  # defines stock text




    def tickers(self, tkr_aftr_entr, begnQuery):
        quotes = ' '

        if begnQuery == True:
            self.quotes.append( str(yf.download(tkr_aftr_entr, period='1d')))
        #quotes = yf.download(tkr_aftr_entr, period='1d')
        quotes= str(self.quotes)
        txt = self.font.render(quotes, True, 'red')  # defines stock text

        x = 0
        y = 200
        for word in self.quotes:  #quotes = wprds
            word_t = self.font.render(word, False, 'black')
            if word_t.get_width() + x <= 880:
                self.stk_screen.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
            else:
                y += word_t.get_height() * 1.1
                x = 0
                self.stk_screen.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
        begnQuery = False
        return begnQuery

    """ 
        def searchBar(self, event):
            rct = pygame.draw.rect(self.stk_screen, 'black', (self.srchRect), 3)  # create search rect object

            srchRect = pygame.Rect(self.srchX, self.srchY, self.srchWdth, self.srchHite)  # defines stk rect
            if event.type == pygame.MOUSEBUTTONDOWN:
                if srchRect.collidepoint(event.pos):
                    txtEnter = True
                    print("iz true")
                else:
                    False
            if event.type == pygame.KEYDOWN:
                print("key down")
                # translate what user wrote into font.render
                self.srchCntent += event.unicode
                print(self.srchCntent)
        """