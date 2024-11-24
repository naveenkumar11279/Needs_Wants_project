import logging
logging.basicConfig(
    filename="app_logfile.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s -%(message)s",
    filemode="a"
)

def get_logger(name):
    return logging.getLogger(name)