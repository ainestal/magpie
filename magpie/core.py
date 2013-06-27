"""
magpie.core
============
magpie core logic 
"""
import logging

from inventory import Inventory

__all__ = ('Magpie', )
log = logging.getLogger(__name__)

class Magpie(object):
    def __init__(self, debug=False):
        log.info('Magpie starting')
        self.inventory = Inventory()

    def sync(self):
        self.inventory.sync()