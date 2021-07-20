from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def Brighter(cst = 0):
    with Image.open("lenna.png") as im:
        image = np.array(im)
        height = image.shape[0]
        width = image.shape[1]
        chanel = image.shape[2]
        cst_np = np.zeros(height *  width * chanel, int).reshape(height, width, chanel) + cst
        new_array = image + cst_np
        new_array[new_array >= 255] = 255
        plt.imshow(new_array)
        plt.show()


def GrayImage():
    with Image.open("lenna.png") as im:
        image = np.array(im)
        new_image = np.dot(image[..., 0 : 3], [0.3,0.59,0.11])
        plt.imshow(new_image,cmap= 'gray')
        plt.show()


def constrast():
    with Image.open("lenna.png") as im:
        image = np.array(im)
        new_image = np.array((image * 1.5), int)
        new_image[new_image >= 255] = 255
        plt.imshow(new_image)
        plt.show()


def ConvertImage():
    with Image.open("lenna.png") as im:
        image = np.array(im)
        plt.imshow(image[:, ::-1])
        plt.show()

    with Image.open("lenna.png") as im:
        image = np.array(im)
        plt.imshow(image[::-1, ::-1])
        plt.show()


def Plus():

    with Image.open("gray.png") as one:
        with Image.open("star.png") as two:
            onez = np.array(one)
            twoz = np.array(two)
            new_image = onez + twoz
            new_image[new_image >= 255] = 255
            plt.imshow(new_image, cmap= 'gray')
            plt.show()


def zero_pad(X, pad):
    X_pad = np.pad(X, ((0, 0), (pad, pad), (pad, pad)), 'constant')
    return X_pad

def sum_np(X, W):
    dot_product = (X * W)
    return np.sum(dot_product)

def Blur():
    W = np.array([[1,2,1], [2,4,2], [1,2,1]]) * 0.0625
    with Image.open("lenna.png") as im:
        image = np.array(im)
        height = image.shape[0]; width = image.shape[1]; chanel = image.shape[2]
        new_image = np.array(image)
        new_array = np.zeros(image.shape, int)
        print(new_array.shape)
        for i in range(1,height - 1):
            for j in range(1,width -1):
                for k in range(chanel):
                    slice_array = new_image[ i-1 : (i + 2),  j - 1 :  j + 2 , k]
                    new_array[i,j, k] = int(sum_np(slice_array, W))
        new_image[new_image >= 255] = 255
        plt.imshow(new_array)
        plt.show()

def main():
    Brighter()
main()