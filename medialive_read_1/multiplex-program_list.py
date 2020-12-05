#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplex-programs.html
if __name__ == '__main__':
    """
	create-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex-program.html
	delete-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex-program.html
	describe-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex-program.html
	update-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html
    """

    parameter_display_string = """
    # multiplex-id : The ID of the multiplex that the programs belong to.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("medialive", "list-multiplex-programs", "multiplex-id", add_option_dict)