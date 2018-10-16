from dataclasses import dataclass
import pygame as pg
import noise
#angle between extremes of vision
viewport_angle = 90
MAX_RAY_ITERS = 50
block_color_lookup = {'air': (155, 201, 255), 'stone': (165, 165, 165)}

@dataclass
class Block:
    typeid: str
    x: int
    y: int
    color: tuple
    
class Player:
    def __init__(self, x , y):
        #2d --- 2 coords
        self.x = x
        self.y = y
        #2d --- 2 look axies
        self.xlook = 0
        self.ylook = 0
        self.look_angle = 0
    
    

    
        

class Game:
    def __init__(self, width, height):
        pg.init()
        self.scr_width = width
        self.scr_height = height
        self.terrain = []
        self.screen = pg.display.set_mode(width, height)
        self.player = Player(0, 0)
    
    def scan(self):
        colorlist = []
        for p in range(self.scr_height):
            colorlist.append(self.raycast(p))
    
    #returns color value for checked spot. Pix goes from 0 (top) to N (bottom)
    def raycast(self, pix):
        relative_angle = (pix/self.scr_height - 0.5) * max #bottom is 1, top is 0
        absolute_angle = player.look_angle + relative_angle
        ray_x = player.x
        ray_y = player.y
        hitblock = 'air'
        for iter in range(MAX_RAY_ITERS):
            ray_x += self.x*math.cos(absolute_angle)
            ray_y += self.y*math.sin(absolute_angle)
            hitblock = world[int(x)][int(y)]
            if hitblock is not None:
                break
        return block_color_lookup[hitblock]  
        
    def run(self):
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return
        self.render()
        
    #send rays for each pixel in the stip
    def render(self):
        #look around
        colors = self.scan()
        for i, col in enumerate(colors):
            py.draw.line(self.screen, col, (i, 0), (i, self.width))
            
        
        pg.display.flip()
class WorldGenerator:
    terrain = []
    world_size = 100000
    base_height = 60
    roughness = 0.84
    base_dis = 55
    iterations = 1
    def gen_world():
        #not sure how useful this is, its probably not.    
        for i in range(self.iterations):
            self.terrain = [self.base_height]*self.world_size
            gen_terrain(0, self.world_size-1, self.base_dis)
            self.terrain = [round(t) for t in self.terrain]
        self.terrain = blur(self.terrain, 2)
        with open('world.csv', 'w') as f:
            wter = csv.writer(f)
            wter.writerow(self.terrain)

        xs = range(len(self.terrain)*100)
        ys = np.repeat(self.terrain, 100)
        plt.plot(xs, ys, 'b')
        plt.xlim((10000, 22000))
        plt.ylim((0, 256))
        plt.show()

        
        
    def blur(arr, iters):
        for i in range(iters):
            for x in range(len(arr)):
                if x != 0 and x < len(arr)-1:
                    arr[x] = round((arr[x-1] + arr[x+1] + arr[x] )/3)
        return arr
    
    #varies up terrain array. arr must be initialised to some number
    def gen_terrain(left_xval, right_xval, displacement):
        if left_xval + 1 == right_xval:
            return
        #find the midpoint.
        mid_xval = math.floor((left_xval + right_xval)/2)
        #generate a value to offset the midpoint by
        #displacment val goes down over time, so change reduces over time
        change = random.random()*2 - 1 #between -1 and 1
        change *= displacement #recursions will make this smaller, reducing change amt
        #midpoint height set to midpoint of left and right heights with change added
        self.terrain[mid_xval] = (self.terrain[left_xval] + self.terrain[right_xval]) / 2 + change
        displacement *= self.roughness
        #repeat for left and right subsets
        gen_terrain(left_xval, mid_xval, displacement)
        gen_terrain(mid_xval, right_xval, displacement)

        