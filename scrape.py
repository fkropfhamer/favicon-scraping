import requests
import csv

def main():

    with open('top-1m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if (row[0] == '20'):
                break 
            
            try:

                r = requests.get(f"https://www.{row[1]}/favicon.ico", allow_redirects=True)
                content_type = r.headers.get('content-type')

                # print(r.headers)

                if (r.status_code == 200):
                    with open(f"./files/{row[1]}.ico", 'wb') as file:
                        file.write(r.content)
            
            except:
                print('something went wrong!', row[1])

if __name__ == "__main__":
    main()
