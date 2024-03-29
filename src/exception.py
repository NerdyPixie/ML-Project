import sys
import logging
import logger

def error_message_detaiL(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = "Error in the script [{0}] at the line number [{1}] with error [{2}]".format(file_name, line_no, error)
    return error


class CustomException(Exception):   
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detaiL(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message   
    