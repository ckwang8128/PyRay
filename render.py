import Image,random

im = Image.new('RGB',(200,200), 'red')

pixel_matrix = im.load()
for i in range(0,200):
    for j in range(0,200):
        pixel_matrix[i,j] = (random.randint(0,255),
                             random.randint(0,255),
                             random.randint(0,255))
im.show()
