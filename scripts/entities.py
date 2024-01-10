import pygame

class PhysicsEntity:
    def __init__(self, game, entity_type, pos, size):
        self.game = game
        self.type = entity_type
        self.pos = list(pos) # allows us to change the position of all
        self.size = size
        self.velocity = [0,0] # x, y represents the speed of the entity
        
        
    def update(self, movement=(0,0)):
        frame_movement = [movement[0] + self.velocity[0], movement[1]+ self.velocity[1]] # add the movement from the frame to the velocity
        
       
        
        self.pos[0] += frame_movement[0] # update the position
        self.pos[1] += frame_movement[1] 
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1) # gravity
    
    def render(self,surf):
        surf.blit(self.game.assets['player'], self.pos)
        