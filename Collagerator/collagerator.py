from PIL import Image
import random
from cloudinary import uploader
from cloudinary import utils
import uploader
def collagerator(images):
	"""
	Parameter: list of image names 
	Returns: link to hosted version of image

	Requires: Python Image Library; pip install Pillow OR visit
	'http://pillow.readthedocs.io/en/3.0.x/installation.html' for more details
	imagemagick; run 'sudo apt-get install imagemagick'

	Program makes a collage of images by overlaying rotated versions of all but 
	the first image on top of the first image provided.

	"""
	final_dims = (500,500)
	first = Image.open(images[0])
	out = first.resize(final_dims)
	tiling = []
	for i in range(len(images)):
		tiling.append(random.randint(0,final_dims[0]/2))

	for i in images[1:]:
		im = Image.open(i).convert('RGBA')
		im = im.rotate(random.randint(0,359), expand=1)

		size = im.size

		if size[0] >= final_dims[0]/1.1:
			newSize1 = size[0]
			
			while newSize1 >= final_dims[0]/1.1:
				newSize1 = int(round(newSize1/1.1))

		else:
			newSize1 = size[0]

		if size[1] >= final_dims[1]/1.1:
			newSize2 = size[1]

			while newSize2 >= final_dims[1]/1.1:
				newSize2 = int(round(newSize2/1.1))
		else:
			newSize2 = size[1]

		box = (newSize1/2,newSize2/2,newSize1+(newSize1/2),newSize2+(newSize2/2))
		region = im.crop(box)
		region = region.resize((newSize1+300,newSize2+300))
		offset = random.choice(tiling)
		tiling.remove(offset)
		out.paste(region, (offset,offset,newSize1+offset+300,newSize2+offset+300), region)

	out.show()
	# out.save('Collagerator/images/final_result.jpg')
	# res = uploader.upload_files("Collagerator/images/final_result.jpg")

	return res


if __name__ == "__main__":
	collagerator(["images/loading.png","images/1.png","images/2.png","images/3.png"])
