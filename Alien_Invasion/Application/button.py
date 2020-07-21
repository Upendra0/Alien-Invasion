import pygame.font

class Button():
    
    def __init__(self, ai_settings, screen, msg, left, top, width, height):
        """
        Create button instance

        Parameters
        ----------
        ai_settings : an setting instance
        screen : Pygame screen surface
        msg : Button name to apper on screen
        (left,top,width,height):pygame Rect

        """
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        #properties of bottons
        self.left=left
        self.top=top
        self.width=width
        self.height=height
        self.botton_color=(230,230,230)
        self.text_color=(0,0,230)
        self.font=pygame.font.SysFont(None, 48)
        self.rect=pygame.Rect(self.left, self.top, self.width, self.height)
        
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        #Create the button name image object
        self.msg_image=self.font.render(msg, True, self.text_color, 
                                        self.botton_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        #First draw the blank rect
        self.screen.fill(self.botton_color, self.rect)
        
        #then render the msg
        self.screen.blit(self.msg_image, self.msg_image_rect)