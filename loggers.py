import logging

main_logger = logging.getLogger(__name__)
handler = logging.FileHandler("logs.log", encoding="utf-8")
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
handler.setFormatter(formatter)
main_logger.addHandler(handler)
main_logger.setLevel(logging.INFO)
