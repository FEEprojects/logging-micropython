import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('test')
sh = logging.StreamHandler()
sh.formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
log.addHandler(sh)

log.info("Test info message")
log.error("Test message4")
log.critical("Test message5")
logging.info("Test message6")

# try:
#     1/0
# except:
#     log.exception("Some trouble (%s)", "expected")
