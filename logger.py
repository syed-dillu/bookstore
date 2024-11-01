import logging as log

log.basicConfig(
    level=log.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%d-%m-%Y %H:%M:%S"

)

log = log.getLogger()

def log_info(message):
    log.info(message)

def log_error(message):
    log.error(message)



