#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-return-shipping-label.html
if __name__ == '__main__':
    """
	describe-return-shipping-label : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/describe-return-shipping-label.html
    """

    parameter_display_string = """
    # job-id : The ID for a job that you want to create the return shipping label for. For example JID123e4567-e89b-12d3-a456-426655440000 .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("snowball", "create-return-shipping-label", "job-id", add_option_dict)





