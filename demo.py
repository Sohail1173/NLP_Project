from Text_Classification.logger import logging
from Text_Classification.exception import CustomException
import sys
# logging.info("Welcome to  out project")

try:
    a=7/"0"
except Exception as e:
    raise CustomException(e,sys) from e