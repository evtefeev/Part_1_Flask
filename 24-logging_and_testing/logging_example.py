import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


app.logger.debug("debug messaage")
app.logger.info("info messaage")
app.logger.warning("warning messaage")
app.logger.error("error messaage")
app.logger.critical("critical messaage")