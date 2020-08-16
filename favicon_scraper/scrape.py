import requests
import csv
import favicon

def main():
    scrape()

def scrape():
    with open('top-1m.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:           
            try:
                print('getting', row[1])

                icons = favicon.get(f"https://www.{row[1]}/", timeout=5)
                icon = icons[0]

                response = requests.get(icon.url, stream=True, timeout=5)
                with open(f'./files/{row[1]}.{icon.format}', 'wb') as image:
                    for chunk in response.iter_content(1024):
                        image.write(chunk)

            except KeyboardInterrupt:
                break

            except:
                print('something went wrong!', row[1])

if __name__ == "__main__":
    main()
