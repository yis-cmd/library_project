import logging

def create_logger(name:str):
    logger = logging.getLogger(name)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)

    return logger