import pygame
from subprocess import call

pygame.init()

SCREEN_WIDTH=500
SCREEN_HIEGHT=500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIEGHT))
pygame.display.set_caption("MENU")

exit_image=pygame.image.load("imgs/exit_btn.png")
race_image=pygame.image.load("imgs/PR_btn.png")
space_image=pygame.image.load("imgs/SSD_btn.png")
snake_image=pygame.image.load("imgs/snake_btn.png")

def open_space():
    call(["python","main.py"])
def open_race():
    call(["python","race.py"])
def open_snake():
    call(["python","snake.py"])    

class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        hieght =image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(hieght*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):

        action = False

        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                action = True
            

        if pygame.mouse.get_pressed()[0]==0:
            self.clicked = False



        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

exit_button = Button(190,350,exit_image,0.5)
race_button = Button(190,50,race_image,0.5)
snake_button = Button(190,150,snake_image,0.5)
space_button = Button(190,250,space_image,0.5)



run = True
while run:

    screen.fill((202,228,241))
    if exit_button.draw():
        run = False
    if race_button.draw():
        open_race()
    if snake_button.draw():
        open_snake()
    if space_button.draw():
        open_space()


    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()


pygame.quit()
