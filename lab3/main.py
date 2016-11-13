from skimage import io, filters, img_as_float
import matplotlib.pyplot as plt
prefix = 'samolot'
extension = '.jpg'
images = []
masks = []
img_indexes = ('01', '17', '16', '07', '08', '10')

for index in img_indexes:
    images.append(io.imread(prefix + index + extension, flatten=True))


for img in images:
    val = filters.threshold_otsu(img_as_float(img))
    masks.append(img < val)


fig, subplots = plt.subplots(ncols=2, nrows=3, squeeze=False, figsize=(30, 15))

it = 0
for i in range(3):
    for j in range(2):
        subplots[i][j].imshow(filters.sobel(img_as_float(masks[it])) ** 0.7, cmap=plt.cm.gray, aspect='auto')
        subplots[i][j].axis('off')
        it += 1

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
