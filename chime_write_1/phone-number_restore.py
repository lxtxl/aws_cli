#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/restore-phone-number.html
if __name__ == '__main__':
    """
	delete-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-phone-number.html
	get-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number.html
	list-phone-numbers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-numbers.html
	update-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html
    """

    parameter_display_string = """
    # phone-number-id : The phone number.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "restore-phone-number", "phone-number-id", add_option_dict)





