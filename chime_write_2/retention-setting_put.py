#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-retention-settings.html
if __name__ == '__main__':
    """
	get-retention-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-retention-settings.html
    """

    parameter_display_string = """
    # account-id : The Amazon Chime account ID.
    # retention-settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "put-retention-settings", "account-id", "retention-settings", add_option_dict)
