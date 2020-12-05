#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex-program.html
if __name__ == '__main__':
    """
	create-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex-program.html
	describe-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex-program.html
	list-multiplex-programs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplex-programs.html
	update-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html
    """

    parameter_display_string = """
    # multiplex-id : The ID of the multiplex that the program belongs to.
    # program-name : The multiplex program name.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("medialive", "delete-multiplex-program", "multiplex-id", "program-name", add_option_dict)
