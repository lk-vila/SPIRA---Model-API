import logging
import os

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    magenta = "\x1b[35;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(levelname)s-%(name)s:   %(message)s"
    format_lineno = "%(levelname)s-%(name)s:   %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: magenta + format_lineno + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format_lineno + reset,
        logging.CRITICAL: bold_red + format_lineno + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def getCustomLogger(name = "root"):
    logger = logging.getLogger(name)
    logger.propagate = False
    
    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())
    
    logger.addHandler(ch)
    
    level = os.getenv("LOGGING_LEVEL")
    if level == "DEBUG":
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    elif level == "INFO":
        logger.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    elif level == "WARNING":
        logger.setLevel(logging.WARNING)
        ch.setLevel(logging.WARNING)
    elif level == "ERROR":
        logger.setLevel(logging.ERROR)
        ch.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.CRITICAL)
        ch.setLevel(logging.CRITICAL)


    return logger
