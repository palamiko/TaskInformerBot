import logging

from bot_app.utils.logging_setup import setup_logging


setup_logging(default_level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug('APP RUN..')
