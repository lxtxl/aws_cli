#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-dedicated-ip-warmup-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # ip : The dedicated IP address that you want to update the warm-up attributes for.
    # warmup-percentage : The warm-up percentage that you want to associate with the dedicated IP address.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint-email", "put-dedicated-ip-warmup-attributes", "ip", "warmup-percentage", add_option_dict)
