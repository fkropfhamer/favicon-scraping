from PIL import Image
import os

def main():
    validate()

        
def validate():
    base_path = './files'

    for filename in os.listdir(base_path):
        print(filename)
        
        if filename.startswith('.'):
            continue

        file_path = (f'{base_path}/{filename}')

        try:
            with Image.open(file_path) as im:
                im.verify()
                # print(im.info)

        except:
            print('image is not valid', file_path)
            os.remove(file_path)
    
    

if __name__ == "__main__":
    main()
