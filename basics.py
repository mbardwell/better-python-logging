import logging
import sys

root = logging.getLogger()
logger = logging.getLogger(__name__)

logger.warning("1. warning")  # 1. warning      # Py2: No handlers could be found for logger "__main__"

logging.basicConfig(level=logging.INFO)  # For root. Creates StreamHandler, adds default Formatter, set logging level to INFO

logger.warning("2. warning")  # WARNING:__main__:2. warning

########################### Handlers

file_h = logging.FileHandler("all.log")
file_h.setLevel(logging.DEBUG)
console_h = logging.StreamHandler(sys.stdout)
console_h.setLevel(logging.INFO)
logger.getEffectiveLevel()   # 20 (INFO)
logger.addHandler(file_h)
logger.addHandler(console_h)
logger.warning("3. warning") # 2x console, 1x file
logger.info("4. info")       # 2x console print, 1x file
logger.debug("5. debug")     # NADA
logger.setLevel(logging.DEBUG)
logger.debug("6. debug")     # 1x console, 1x file (WHAT)
root_h = root.handlers[0]    # <StreamHandler <stderr> (NOTSET)>
root_h.setLevel(logging.INFO)
logger.debug("7. debug")     # 1x file (Ahh peace and quiet)


########################### Filters

class StringContainsFilter(logging.Filter):
    from typing import List
    def __init__(self, params: List[str]):
        """
        params: ["a", "b"]
        string: "bcd" -> b in string, filter string
        string: "cc" -> a, b not in string, do not filter string
        """
        self.params = params

    def filter(self, record: logging.LogRecord):
        #  if the record contains the string, return false
        #  "if true let it through"
        #  for you nerds think high pass filter, not coffee grounds filter
        return not any([param in record.getMessage() for param in self.params])
logger.addFilter(StringContainsFilter(["weather problem"]))
logger.info("C1 launches today!")
logger.info("There is a weather problem")


########################### Formatters

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_h.setFormatter(formatter)
console_h.setFormatter(formatter)


########################### Configuring (will finish...)

from logging import config  # why logging.config doesn't work, idk...
from pathlib import Path

import yaml  # pip install pyyaml

# this double prints everything from before. I don't know why
# but usually this would be near the top of your main file so
# it doesn't matter
with open(Path(__file__).parent / "logging.conf", "r") as f:
    config.dictConfig(yaml.safe_load(f.read()))

logger.info("I like jam")           # console prints
logger.info("I like peanut butter") # does not print (see filter in logging.conf)