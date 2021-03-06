#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html
if __name__ == '__main__':
    """
	create-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex-program.html
	delete-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex-program.html
	describe-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex-program.html
	list-multiplex-programs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplex-programs.html
    """

    parameter_display_string = """
    # multiplex-id : The ID of the multiplex of the program to update.
    # program-name : The name of the program to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("medialive", "update-multiplex-program", "multiplex-id", "program-name", add_option_dict)
