import logging
import requests


logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def scrape(self):
        """ Gives the text from ACA website """

        url = 'https://www.worldometers.info/coronavirus/'
        response = requests.get(url)

        if not response.ok:
            # log the error
            logger.error(response.text)

        else:
            # Note: here json can be used as response.json
            data = response.text

            # save scraped objects here
            # you can save url to identify already scrapped objects
            self.storage.save_raw_data(data)

