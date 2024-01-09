class Tilemap:
    def __init__(self, tile_size=16):
       self.tile_size = tile_size
       self.tilemap = {}    # dictionary of tiles
       self.offgrid_tiles = []  # tiles that are not on the grid
       
       for i in range(10):
           self.tilemap[str(3 + i)+ ';10'] ={'type' : 'grass', 'variant' : '1', 'pos' : (3 + i, 10)}
           self.tilemap['10;' + str(5 + i)] = {'type' : 'stone', 'variant' : '1', 'pos' : (10, 5 + i)}
           
    
    