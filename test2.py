from noise import pnoise1
import random, csv, math
import numpy as np
import matplotlib.pyplot as plt
world_size = 100000
base_height = 60
roughness = 0.84
base_dis = 55
iterations = 1
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
    terrain[mid_xval] = (terrain[left_xval] + terrain[right_xval]) / 2 + change
    displacement *= roughness
    #repeat for left and right subsets
    gen_terrain(left_xval, mid_xval, displacement)
    gen_terrain(mid_xval, right_xval, displacement)

#not sure how useful this is, its probably not.    
for i in range(iterations):
    terrain = [base_height]*world_size
    gen_terrain(0, world_size-1, base_dis)
    terrain = [round(t) for t in terrain]


def blur(arr, iters):
    for i in range(iters):
        for x in range(len(arr)):
            if x != 0 and x < len(arr)-1:
                arr[x] = round((arr[x-1] + arr[x+1] + arr[x] )/3)
    return arr
terrain = blur(terrain, 2)
with open('world.csv', 'w') as f:
    wter = csv.writer(f)
    wter.writerow(terrain)

xs = range(len(terrain)*100)
ys = np.repeat(terrain, 100)
plt.plot(xs, ys, 'b')
plt.xlim((10000, 22000))
plt.ylim((0, 256))
plt.show()
