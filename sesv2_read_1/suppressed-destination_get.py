#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-suppressed-destination.html
if __name__ == '__main__':
    """
	delete-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-suppressed-destination.html
	list-suppressed-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-suppressed-destinations.html
	put-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-suppressed-destination.html
    """

    parameter_display_string = """
    # email-address : The email address thatâs on the account suppression list.
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

    execute_one_parameter("sesv2", "get-suppressed-destination", "email-address", add_option_dict)