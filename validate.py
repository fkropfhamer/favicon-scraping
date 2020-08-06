from PIL import Image
import os

def validate(path):
    try:
        
        with Image.open(path) as im:
            im.verify()
            print(im.info)


    except:
        print('image is not valid', path)
        os.remove(path)

        
def main():
    base_path = './files'

    for filename in os.listdir(base_path):
        print(filename)
        validate(f'{base_path}/{filename}')
    
    

if __name__ == "__main__":
    main()
