from favicon_scraper.scrape import scrape
from favicon_scraper.to_numpy import save_to_numpy
from favicon_scraper.validate import validate

def main():
    scrape()
    validate()
    save_to_numpy()

if __name__ == "__main__":
    main()
