import pygame

def main():
    # initialize the pygame.
    pygame.init()

    # the screen size setting.
    screen=pygame.display.set_mode((800,600))
    # set title name.
    pygame.display.set_caption("ball")
    x, y = 50, 50
    # pygame.draw.circle(screen,(0,255,0),(300,300),50,0)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running=False
        # fill the color to the whole screen.
        screen.fill((244, 244, 244))
        # load image
        lena_image=pygame.image.load("D:\\lena.jpg")
        # draw it on the specified location.
        screen.blit(lena_image,(x,y))
        # refresh the screen.
        pygame.display.flip()

        pygame.time.delay(50)
        x,y =x+5,y+5


if __name__ == '__main__':
    main()