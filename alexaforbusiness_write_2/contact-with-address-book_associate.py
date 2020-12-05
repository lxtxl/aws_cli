#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/associate-contact-with-address-book.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # contact-arn : The ARN of the contact to associate with an address book.
    # address-book-arn : The ARN of the address book with which to associate the contact.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "associate-contact-with-address-book", "contact-arn", "address-book-arn", add_option_dict)
