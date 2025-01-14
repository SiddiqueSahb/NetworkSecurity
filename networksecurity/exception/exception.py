import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):  # Custom exception class inheriting from Python's base Exception class
    def __init__(self, error_message, error_details: sys):  # Constructor to initialize error message and details
        self.error_message = error_message  # Storing the provided error message
        _, _, exc_tb = error_details.exc_info()  # Extracting traceback information from error_details
        self.line_no = exc_tb.tb_lineno  # Line number where the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the exception occurred

    def __str__(self):  # Overriding the string representation method for better error description
        return "Error occurred in Python script: [{0}] Line number: [{1}] Error message: [{2}]".format(
            self.file_name, self.line_no, str(self.error_message)  # Formatting the error details into a readable string
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
