import logging.config

from clients.EndOfLifeDateClient import EndOfLifeDateClient
from utils.Utils import isEOL

logging.config.fileConfig('./config/logging.conf')

class EOLScrapper:
    def __init__(this) -> None:
        this.__logger = logging.getLogger(__name__)
        this.__logger.info("{} initialized".format(__name__))
        
    def doScrape(this, products:list):
        edl = EndOfLifeDateClient()
        
        if products is None:
            products = edl.listAllProducts()
        
        for product in products:
            cycleList = edl.getProductDetails(product=product)
            for cycle in cycleList:
                try:
                    if isEOL(cycle['eol']):
                        this.__logger.info("TPL: {}, Version: {}, EOL-Date:{}, EOL?: {}".format(product, cycle['cycle'], cycle['eol'], isEOL(cycle['eol'])))
                except Exception as e:
                    this.__logger.error(e, exc_info=True)
                    
        this.__logger.info("scraping complete")
        

if __name__ == '__main__':
    scraper = EOLScrapper()
    scraper.doScrape(['spring-boot', 'spring-framework'])