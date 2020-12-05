#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-suppressed-destination.html
if __name__ == '__main__':
    """
	delete-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-suppressed-destination.html
	get-suppressed-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-suppressed-destination.html
	list-suppressed-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-suppressed-destinations.html
    """

    parameter_display_string = """
    # email-address : The email address that should be added to the suppression list for your account.
    # reason : The factors that should cause the email address to be added to the suppression list for your account.
Possible values:

BOUNCE
COMPLAINT
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "put-suppressed-destination", "email-address", "reason", add_option_dict)
