#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/delete-protection.html
if __name__ == '__main__':
    """
	create-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html
	describe-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection.html
	list-protections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html
    """

    parameter_display_string = """
    # protection-id : The unique identifier (ID) for the  Protection object to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("shield", "delete-protection", "protection-id", add_option_dict)





