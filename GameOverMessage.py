import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (105, 105, 105)

class PopUp():
    def __init__(self, text, x=0, y=0, width=100, height=50, command=None):
        pygame.init()

        # Object Text
        self.text = text
        self.font1 = pygame.font.SysFont('Arial', int(0.1*width))
        self.text_width, self.text_height = self.font1.size(self.text)

        self.command = command

        # Object Surface
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(WHITE)

        # Object Border
        self.border = pygame.draw.rect(self.image_normal, BLUE, pygame.Rect(0, 0, width, height), 5, 5, 5, 5)

        # Object Button
        self.buttonW = 0.2*width
        self.buttonH = 0.1*height
        self.button = pygame.draw.rect(self.image_normal, GRAY, [width/2 - self.buttonW/2, 2*height/3 - self.buttonH/2, self.buttonW, self.buttonH])
        self.btnText = "RESTART"
        self.font2 = pygame.font.SysFont('Arial', int(0.2*self.buttonW))
        self.btnText_width, self.btnText_height = self.font2.size(self.btnText)

        # Draw Text Object
        self.image_normal.blit(self.font1.render(self.text, True, BLACK), (width/2 - self.text_width/2, height/3 - self.text_height/2))
        self.image_normal.blit(self.font2.render(self.btnText, True, WHITE), (width / 2 - self.buttonW/2 + (self.buttonW - self.btnText_width)/2,  2*height/3 - self.buttonH/2 + (self.buttonH - self.btnText_height)/2))

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        # you can't use it before `blit`
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            posX = pos[0] - self.rect.topleft[0]
            posY = pos[1] - self.rect.topleft[1]
            # print(posX, posY)
            buttonLeft = self.button.x
            buttonRight = self.button.x + self.buttonW
            buttonTop = self.button.y
            buttonBottom = self.button.y + self.buttonH
            # print("Width Borders:", buttonLeft, buttonRight)
            # print("Height Borders:", buttonTop, buttonBottom)
            if buttonLeft < posX < buttonRight and buttonTop < posY < buttonBottom:
                # if self.command:
                #     self.command
                return False