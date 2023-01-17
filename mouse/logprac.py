import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("이거 뭐야")
# logging.info("ready...")
# logging.warning("이 프로그램은 구 버전 파이썬을 사용하고 있습니다. 현 버전에서 제대로 실행되지 않을 수 있습니다.")
# logging.error("에러가 발생하였을 수도 있습니다.")
# logging.critical("해당 파일이 존재하지 않습니다. \n프로그램을 종료합니다")

logFor = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
streamH = logging.StreamHandler()
streamH.setFormatter(logFor)
logger.addHandler(streamH)
filename = datetime.now().strftime("logfile_%Y%m%d%H%M%S.log")
fileH = logging.FileHandler(filename, encoding="utf-8")
fileH.setFormatter(logFor)
logger.addHandler(fileH)

logging.debug("test and test")