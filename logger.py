import logging as log
import os
from datetime import datetime
from pathlib import Path

if not os.path.exists("logs"):
    os.mkdir("logs")

log_file = Path("logs") / f"log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

log.basicConfig(
    filename= log_file,
    level=log.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%d-%m-%Y %H:%M:%S"

)

log = log.getLogger()

def log_info(message):
    log.info(message)

def log_error(message):
    log.error(message)



