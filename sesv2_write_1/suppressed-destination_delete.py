#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-suppressed-destination.html
if __name__ == '__main__':
    """
	get-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-suppressed-destination.html
	list-suppressed-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-suppressed-destinations.html
	put-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-suppressed-destination.html
    """

    parameter_display_string = """
    # email-address : The suppressed email destination to remove from the account suppression list.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "delete-suppressed-destination", "email-address", add_option_dict)





