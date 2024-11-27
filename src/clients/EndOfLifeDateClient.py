import logging
import json
import requests

class EndOfLifeDateClient:
    def __init__(this) -> None:
        this.__logger = logging.getLogger(__name__)
        this.__logger.info("{} initialized".format(__name__))
    
    def listAllProducts(this) -> list:
        response = requests.request("GET", "https://endoflife.date/api/all.json", headers={'Accept': 'application/json'})
        if response.ok:
            return json.loads(response.text)
        else:
            this.__logger.warning("Attempt to fetch list of all products returned status: {}".format(response.status_code))
            return list()
    
    def getProductDetails(this, product) -> list:
        response = requests.request("GET", "https://endoflife.date/api/{}.json".format(product), headers={'Accept': 'application/json'})
        if response.ok:
            return json.loads(response.text)
        else:
            this.__logger.warning("Attempt to fetch details of product: {} returned status: {}".format(product, response.status_code))
            return list()
        
    def getProductCycleDetails(this, product, cycle) -> list:
        response = requests.request("GET", "https://endoflife.date/api/{}/{}.json".format(product, cycle), headers={'Accept': 'application/json'})
        if response.ok:
            return json.loads(response.text)
        else:
            this.__logger.warning("Attempt to fetch details of product: {}, cycle: {} returned status: {}".format(product, cycle, response.status_code))
            return list()