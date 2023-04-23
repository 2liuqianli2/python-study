import logging

logger=logging.getLogger(__name__)

header=logging.FileHandler("./log.txt",encoding="utf-8")

formatter=logging.Formatter("%(asctime)s--%(levelname)s--%(lineno)d--%(message)s")

logger.addHandler(header)

header.setFormatter(formatter)

logger.debug("debug")
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')