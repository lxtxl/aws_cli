#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact-list.html
if __name__ == '__main__':
    """
	create-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact-list.html
	delete-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact-list.html
	get-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact-list.html
	list-contact-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contact-lists.html
    """

    parameter_display_string = """
    # contact-list-name : The name of the contact list.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "update-contact-list", "contact-list-name", add_option_dict)





