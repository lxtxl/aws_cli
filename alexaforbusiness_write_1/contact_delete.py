#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-contact.html
if __name__ == '__main__':
    """
	create-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-contact.html
	get-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-contact.html
	search-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-contacts.html
	update-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-contact.html
    """

    parameter_display_string = """
    # contact-arn : The ARN of the contact to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "delete-contact", "contact-arn", add_option_dict)





