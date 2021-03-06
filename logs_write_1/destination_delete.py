#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-destination.html
if __name__ == '__main__':
    """
	describe-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-destinations.html
	put-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-destination.html
    """

    parameter_display_string = """
    # destination-name : The name of the destination.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "delete-destination", "destination-name", add_option_dict)





