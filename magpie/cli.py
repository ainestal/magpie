"""
magpie.cli
============
command-line entry
"""
import logging
import sys
import argparse

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
    print('this is a test')
    sys.exit()
    # sys.exit(Magpie(debug=args.debug).sync())
