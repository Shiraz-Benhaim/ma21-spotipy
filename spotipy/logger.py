import logging


def create_logger():
    log = logging.getLogger('spotify_logger')
    log.setLevel(logging.DEBUG)

    # warning and the higher log levels will be printed to a file
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    log.addHandler(fh)
    return log
