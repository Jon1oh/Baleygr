import logging
import os

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(
        logging.FileHandler(os.path.join(os.path.dirname(__file__), log_file))
    )

    handlers = [
        logging.FileHandler(os.path.join(os.path.dirname(__file__), log_file)),
        logging.StreamHandler(),
    ]

    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


root_logger = setup_logger("", "root.log")
generator_logger = setup_logger("generator", "generator.log")
crawler_logger = setup_logger("crawler", "crawler.log")
classifier_logger = setup_logger("classifier", "classifier.log")
