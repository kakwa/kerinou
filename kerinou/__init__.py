import os
import kerinou.views
from flask import Flask

app = Flask(__name__)
app.config.from_object('kerinou.default_settings')
app.config.from_envvar('KERINOU_SETTINGS')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    logfile = os.path.join(app.config['LOG_DIR'], 'kerinou.log')
    file_handler = TimedRotatingFileHandler(logfile, 'midnight')
    file_handler.setLevel(logging.WARNING)
    logformat = logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s')
    file_handler.setFormatter(logformat)
    app.logger.addHandler(file_handler)
