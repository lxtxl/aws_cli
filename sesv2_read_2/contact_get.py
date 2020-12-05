#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact.html
if __name__ == '__main__':
    """
	create-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact.html
	delete-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact.html
	list-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contacts.html
	update-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact.html
    """

    parameter_display_string = """
    # contact-list-name : The name of the contact list to which the contact belongs.
    # email-address : The contactâs email addres.
    """

    execute_two_parameter("sesv2", "get-contact", "contact-list-name", "email-address", parameter_display_string)