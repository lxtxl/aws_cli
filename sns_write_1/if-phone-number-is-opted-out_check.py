#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/check-if-phone-number-is-opted-out.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # phone-number : The phone number for which you want to check the opt out status.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sns", "check-if-phone-number-is-opted-out", "phone-number", add_option_dict)





