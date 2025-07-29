import sys
from  src.logger import logging 
def error_message_detail(error, error_detail:sys):

    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] with message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error_message_detail(error, error_detail))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        1 / 0  # Example to raise an exception
    except Exception as e:
        logging.info(f"Divide by zero error occurred: {e}")
        raise CustomException(e, sys) from e    