from skimage import io, filters, img_as_float
from scipy import ndimage
import matplotlib.pyplot as plt
prefix = 'kostki01'
extension = '.png'
img = io.imread(prefix + extension, flatten=True)
val = filters.threshold_otsu(img_as_float(img))
print(val)
mask = (img < 0.25)
# mask = filters.inverse(mask)
labeled, nr_objects = ndimage.label(img < 0.25)
print(nr_objects)

io.imshow(mask)
io.show()
