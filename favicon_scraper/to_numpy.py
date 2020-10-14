import numpy as np
import os
from PIL import Image

def main():
    save_to_numpy()

def save_to_numpy():
    base_path = './files'

    numpy_arrays = None

    for filename in os.listdir(base_path):
        try:
            with Image.open(f'{base_path}/{filename}') as im:
                resized = im.resize((32, 32))
                resizedRGB = resized.convert(mode='RGB')

                imageArray = np.array(resizedRGB)
                imageArray = imageArray.reshape((1, 32, 32, 3))

                if imageArray.shape != (1, 32, 32, 3):
                    print('wrong shape')

                if numpy_arrays is None:
                    numpy_arrays = imageArray
                    continue
            
                numpy_arrays = np.append(numpy_arrays, imageArray, axis=0)
        except:
            print('something went wrong')

    print(numpy_arrays.shape)

    np.save('./favicons.npy', numpy_arrays)


if __name__ == "__main__":
    main()