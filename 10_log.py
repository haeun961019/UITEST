import pyautogui

import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format = "%(asctime)s  [%(levelname)s] %(message)s")
#logging.basicConfig(level=logging.ERROR, format = "%(asctime)s  [%(levelname)s] %(message)s")

#debug < info < warning < error < critical
logging.debug("아 이건 누가 짠거야")
logging.info("자동화 수행 준비")
logging.warning("이 스크립트는 조금 오래됐습니다. 실행 상 문제 있을 수 있어요")
logging.error("에러발생, 에러 코드는 ...")
logging.critical("복구불가능")

# 터미널과 파일에 함께 로그 남기기
import logging

#시간 로그레벨 메시지 형태로 로그 작성
logFormatter = logging.Formatter("%(asctime)s  [%(levelname)s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#파일
filename = datetime.now().strftime("log_%Y%m%d%H%M%S.log") #log_20211010141011.log
fileHandler = logging.FileHandler(filename, encoding = 'utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그 남기는 테스트 진행")