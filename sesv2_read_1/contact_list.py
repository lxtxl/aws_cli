#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contacts.html
if __name__ == '__main__':
    """
	create-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact.html
	delete-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact.html
	get-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact.html
	update-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact.html
    """

    parameter_display_string = """
    # contact-list-name : The name of the contact list.
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

    execute_one_parameter("sesv2", "list-contacts", "contact-list-name", add_option_dict)