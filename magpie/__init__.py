"""
magpie
========
Monitor AWS resource usage and cut costs
"""
import logging
try:
    from logging import NullHandler
except ImportError:
    # py26
    try:
        from logutils import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass

__version__ = '0.1-dev'
__versioninfo__ = __version__.split('.')
__all__ = ()

logging.getLogger(__name__).addHandler(NullHandler())
