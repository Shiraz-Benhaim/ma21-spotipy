import logging


def create_logger():
    log = logging.getLogger('spotify_logger')
    log.setLevel(logging.DEBUG)

    # debug and info messages will be printed to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # warning and the higher log levels will be printed to a file
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    log.addHandler(fh)
    log.addHandler(ch)

    return log
