#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-address-book.html
if __name__ == '__main__':
    """
	create-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-address-book.html
	get-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-address-book.html
	search-address-books : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-address-books.html
	update-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-address-book.html
    """

    parameter_display_string = """
    # address-book-arn : The ARN of the address book to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "delete-address-book", "address-book-arn", add_option_dict)





