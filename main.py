"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather
python3 -m main parse

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import sys
import logging

from scraper import Scraper
from storage import Persistor
from parser import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = 'scrapped_data.txt'
TABLE_FORMAT_FILE = 'data.csv'


def gather():
    logger.info("gather")
    storage = Persistor(SCRAPPED_FILE)
    scrapper = Scraper(storage)
    scrapper.scrape()


def parse():
    # parse gathered data and save as csv

    logger.info("parse")
    storage = Persistor(SCRAPPED_FILE,TABLE_FORMAT_FILE)
    parser = Parser()

    raw_data = storage.read_raw_data()
    parsed_file = parser.parse_object(raw_data)
   #parsed_files = [parser.parse_object(file) for file in raw_data]
    storage.save_csv(parsed_file)


def stats():
    """ If you have time, you can calculate some statistics on the data gathered """
    logger.info("stats")

    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':
    """
    What does the line above mean
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather()

    elif sys.argv[1] == 'parse':
        parse()

    logger.info("work ended")
