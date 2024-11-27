import argparse, configparser, json, logging.config
import concurrent.futures
from utils.Utils import isEOL

from clients.EndOfLifeDateClient import EndOfLifeDateClient

logging.config.fileConfig('./config/logging.conf')

class EOLScrapper:
    def __init__(this) -> None:
        this.__logger = logging.getLogger(__name__)
        this.__logger.info("{} initialized".format(__name__))
        
    def doScrape(this, products:list):
        edl = EndOfLifeDateClient()
        
        for product in products:
            cycleList = edl.getProductDetails(product=product)
            for cycle in cycleList:
                this.__logger.info("TPL: {}, Version: {}, EOL-Date:{}, EOL?: {}".format(product, cycle['cycle'], cycle['eol'], isEOL(cycle['eol'])))
                
        this.__logger.info("scraping complete")
        

if __name__ == '__main__':
    scraper = EOLScrapper()
    scraper.doScrape(["spring-boot"])