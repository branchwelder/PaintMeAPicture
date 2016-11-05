from PIL import Image
import random
def collogerator(images):
	#Takes a list of image names as a parameter and returns a collage of those images
	final_dims = (500,500)
	first = Image.open(images[0])
	out = first.resize(final_dims)
	tiling = []
	for i in range(len(images)):
		tiling.append(random.randint(0,final_dims[0]/2))

	for i in images[1:]:
		im = Image.open(i)
		size = im.size

		if size[0] >= final_dims[0]/2:
			newSize1 = size[0]
			
			while newSize1 >= final_dims[0]/2:
				newSize1 = int(round(newSize1/4))

		if size[1] >= final_dims[1]/1.5:
			newSize2 = size[1]

			while newSize2 >= final_dims[1]/1.5:
				newSize2 = int(round(newSize2/4))
		
		box = (newSize1/4,newSize2/4,newSize1+(newSize1/4),newSize2+(newSize2/4))
		region = im.crop(box)
		
		offset = random.choice(tiling)
		tiling.remove(offset)
		out.paste(region, (offset,offset,newSize1+offset,newSize2+offset))

	out.show()

if __name__ == "__main__":
	collogerator(["images/loading.png","images/1.png","images/2.png","images/3.png"])


	#place 1: images randomly within bounds of first image