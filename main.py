import pygame
import buttons #this is used when instantiating
import front_pg_tickers
import stockAdder
import tutorial
import time
import os




# base class

def main():
    pygame.init()
    screenHeight = 1000
    screenWidth = 1080
    #print(pygame.font.get_fonts())
    screen = pygame.display.set_mode((1000,1080))

    # -------------- instantiate --------------
    btn = buttons.Button()
    tkr = front_pg_tickers.tickers()
    stkAdder = stockAdder.stock_adder() #call class that is used to display page where stocks can be added
    tut = tutorial.Tutorial()



        # --------------define buttons and their text --------------
    font = pygame.font.SysFont('helveticaneue', 22)  # name size bold ital
    # define start button
    strTxt = font.render('Search stocks', True, 'white') #defines start text
    startBtn = pygame.Rect(btn.start_btn())  #defines start rect

    # Define alt button
    newsTxt = font.render('News', True, 'white') #defines alt txt
    newsBtn = pygame.Rect(btn.news()) #defines alt rect

    #define stock button
    trndTxt = font.render('Trending', True, 'white')#defines stock text
    trndBtn = pygame.Rect(btn.Trending())  #defines stk rect

    #define ticker tab
    tkrTab = pygame.Rect(tkr.boxOutline())

    #define add stock button
    addTxt = font.render('+', True, 'black')  # defines + button in the middle of the add circle




    menuLoop = True  # Conditional sentinel to run pygame loop
    while menuLoop:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((255, 255, 255)) #133,112,218


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuLoop = False

            ###??
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startBtn.collidepoint(event.pos):
                    stkAdder.runPage()
                    #print("I dont wanna see dis")

            # draw the popual tickers on the front page, left side
            pygame.draw.rect(screen, btn.butn_color(), tkrTab)#,3)#  #<-pygame.Rect(btn.stk()) -< return (self.stkbutnX, self.stkbutnY, self.butnWdth, self.butnHeit)
            addY = 0  # used to put space between different tickers and the title
            for x in tkr.tkr_txt():
                screen.blit(x, (tkr.tabX, tkr.tabY+addY))
                addY +=50

            # --------- tutorial ---------
                #tut.displayTut()
                #tutBox1 = pygame.Rect(tut.displayTut())
                #pygame.draw.rect(screen, (255,255,255), tutBox1 )
                # blit: draws a source Surface onto this Surface.
                tutTxt = font.render(tut.tutBox1, True, 'red')  # defines start text
                pygame.draw.rect(screen, (255, 255, 255), tut.displayTut())
                screen.blit(tutTxt , (tut.boxX, tut.boxY))

            # __________ decorate top line __________
            pygame.draw.line(screen,'black',(0,90),(screenWidth,90)) #line(surface, color, start_pos, end_pos) -> Rect
            pygame.draw.line(screen,'black',(300 +20,90),(300 +20,screenHeight )) #line(surface, color, start_pos, end_pos) -> Rect


            #__________ buttons ____________

            addBtn = pygame.draw.circle(screen, (123, 133, 125), (btn.centerX, btn.centerY),
                                        btn.radius)  # (surface, color, center, radius) -> Rect
            screen.blit(addTxt, (btn.centerX, btn.centerY))  # blit(source, dest, area=None, special_flags=0) -> Rect
            # pygame.draw.rect(screen, btn.butn_hvr_color(), stkBtn)

            #Trending button
            if btn.stkbutnX <=  mouse_pos[0] <= (btn.stkbutnX + btn.butnWdth) and btn.stkbutnY <=  mouse_pos[1] <= (btn.stkbutnY + btn.butnHeit) :
                pygame.draw.rect(screen, btn.butn_hvr_color(), trndBtn)
                # draw start string to start box
                screen.blit(trndTxt, (btn.stkbutnX, btn.stkbutnY))  # blit(source, dest, area=None, special_flags=0) -> Rect

            #mouse not in start box
            else:
                pygame.draw.rect(screen, btn.butn_color(), trndBtn)
                # blit: draws a source Surface onto this Surface.
                screen.blit(trndTxt, (btn.stkbutnX, btn.stkbutnY))  # blit(source, dest, area=None, special_flags=0) -> Rect



            #news button
            if btn.altbutnX <=  mouse_pos[0] <= (btn.altbutnX + btn.butnWdth) and btn.altbutnY <=  mouse_pos[1] <= (btn.altbutnY + btn.butnHeit) :
                pygame.draw.rect(screen, btn.butn_hvr_color(), newsBtn)
                # draw start string to start box
                screen.blit(newsTxt, (btn.altbutnX, btn.altbutnY))  # blit(source, dest, area=None, special_flags=0) -> Rect
            #mouse not in start box
            else:
                pygame.draw.rect(screen, btn.butn_color(), newsBtn)
                # blit: draws a source Surface onto this Surface.
                screen.blit(newsTxt, (btn.altbutnX, btn.altbutnY))  # blit(source, dest, area=None, special_flags=0) -> Rect


            #start hover
            #make start box change color
            if btn.butnX <=  mouse_pos[0] <= (btn.butnX + btn.butnWdth) and btn.butnY <=  mouse_pos[1] <= (btn.butnY + btn.butnHeit) :
                pygame.draw.rect(screen, btn.butn_hvr_color(), startBtn)
                # draw start string to start box
                screen.blit(strTxt, (btn.butnX, btn.butnY))  # blit(source, dest, area=None, special_flags=0) -> Rect
            #mouse not in start box
            else:
                pygame.draw.rect(screen, btn.butn_color(), startBtn)
                # blit: draws a source Surface onto this Surface.
                screen.blit(strTxt, (btn.butnX, btn.butnY))  # blit(source, dest, area=None, special_flags=0) -> Rect
            #end start box changes color

            #update screen
            pygame.display.flip() #moved flip from  inside if else statements down here and that stoped the flickering
pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()