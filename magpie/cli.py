"""
magpie.cli
============
command-line entry
"""
import logging
import sys
import argparse

from core import Magpie

__all__ = ('run',)
log = logging.getLogger(__name__)


def run():
    bootstrap_parser = argparse.ArgumentParser(description='Magpie CLI tool')
    bootstrap_parser.add_argument('--debug', action='store_true')
    args = bootstrap_parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig()
        
    sys.exit(Magpie(debug=args.debug).sync())

if __name__ == '__main__':
    run()