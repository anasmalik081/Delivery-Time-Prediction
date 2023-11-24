"""
Script for Custom exception handling
"""

# importing libraries
import os, sys


# creating customexception class
class CustomException(Exception):
    # constructor
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_details(error_message, error_details)
    

    # method to get error message details
    def error_message_details(self, error, error_details):
        _,_,exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        exc_lineno = exc_tb.tb_frame.f_lineno
        tb_lineno = exc_tb.tb_lineno

        error_message = f"""
            Error occured in execution of :
            [{file_name}] at
            try block line number: [{tb_lineno}]
            and exception block line number: [{exc_lineno}]
            error: [{error}]
        """

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
