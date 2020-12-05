#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact.html
if __name__ == '__main__':
    """
	delete-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact.html
	get-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact.html
	list-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contacts.html
	update-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact.html
    """

    parameter_display_string = """
    # contact-list-name : The name of the contact list to which the contact should be added.
    # email-address : The contactâs email address.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "create-contact", "contact-list-name", "email-address", add_option_dict)
