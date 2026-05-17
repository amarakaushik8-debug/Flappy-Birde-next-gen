import pygame as pg

class Bird(pg.sprite.Sprite):#inheriting sprite class
    def __init__(self,scale_factor):
        super(Bird,self).__init__()#inherits'Bird'from sprite class
        self.img_list=[pg.transform.scale_by(pg.image.load('background/birdup.png').convert_alpha(),scale_factor),pg.transform.scale_by(pg.image.load('background/birddown.png').convert_alpha(),scale_factor)]#making a list of two images of bird(convert alpha is used to make image transparent with no black pixels seen
        self.image_index=0
        self.image=self.img_list[self.image_index]#giving the sprite an image of brid from the list above using above index
        self.rect=self.image.get_rect(center=(100,100))#getting a variable which stores its position
        self.y_velocity=0#applying initial velocity
        self.gravity=10#applying gravity
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=False

    def update(self,dt):
        if self.update_on:
           self.applyAnimation()
           self.applyGravity(dt)

           if self.rect.y<=0:#if the bird touches the top of window it gets stuck over there to avoid it we use this logic
              self.rect.y=0
              self.flap_speed=0#speed will become 0 and thus will fall down hence won't get stuck on top
           elif self.rect.y>=0 and self.flap_speed==0:
               self.flap_speed=250




    def applyGravity(self,dt):
        self.y_velocity += self.gravity * dt #'y' position has to be changed and it is'+=' due to coordinate system of pygame is different
        self.rect.y += self.y_velocity#gives speed to bird by using gravity and dt.

    def flap(self,dt):
        self.y_velocity= -self.flap_speed*dt#using flap_speed to decrease the speed.Here '-ve' is used because as spacebar is clicked bird will fly up.

    def applyAnimation(self):
        if self.anim_counter==5:#this step is used for switching between the two images of birds to make an effect that it is flying really.
            self.image=self.img_list[self.image_index]
            if self.image_index==0: self.image_index=1
            else:self.image_index=0
            self.anim_counter=0#as soon as counter==5 it will become 0 here and strat from beginning again.

        self.anim_counter += 1

    def resetPosition(self):
        self.rect.center = (100, 100)
        self.y_velocity=0
        self.anim_counter=0









