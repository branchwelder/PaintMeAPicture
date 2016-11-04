from PIL import Image
def collogerator(images):
	#Takes a list of images as a parameter and returns a collage of those images
	
	first = Image.open(images[0])
	out = first.resize((400, 400))
	for i in images[1:]:
		im = Image.open(i)
		size = im.size
		# box = (0, 0, 191, 175)
		box = (0,0,size[0],size[1])
		region = im.crop(box)
		first.paste(region, box)

	first.show()

if __name__ == "__main__":
	collogerator(["images/loading.png"])