from PIL import Image

def create_thumbnail(file,size):
   with Image.open(file) as im:
      im_thumb = im.copy()
      im_thumb.thumbnail((size,size))
      im_thumb.save("thumbnail-" + file,im.format)
      im_thumb.show()