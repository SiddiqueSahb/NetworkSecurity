import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.line_no = exc_tb.tb_lineno  # Corrected variable name
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # Corrected attribute name

    def __str__(self):
        return "Error occurred in Python script: [{0}] Line number: [{1}] Error message: [{2}]".format(
            self.file_name, self.line_no, str(self.error_message)
        )
"""
if __name__ == '__main__':
    try:
        logger.logging.info("Enter try block")  # Fixed logger usage
        a = 1 / 0  # This will trigger a ZeroDivisionError
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
        
"""        
