"""
magpie.inventory
============
The inventory main class containing main inventory logic
"""
import logging

from aws.emr import EMRInventory

log = logging.getLogger(__name__)

class Inventory():
    def __init__(self):
        log.info('Initializing inventory class')

    def sync(self):
        emrInventory = EMRInventory()
        emrInventory.list_current_resources()