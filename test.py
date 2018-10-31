#画像の読み込み

images = []
path = 'C:/Users/koji_yamamoto/Desktop/自習/hiragana73/U304A/'
for i in os.listdir(path):
    images.append(path + str(i))
    

plt.figure(figsize = (20,20))
for i, file in enumerate(images[:20]):
    img = Image.open(file)
    im = np.array(img)
    plt.subplot(5,4, i + 1)
    plt.imshow(im)