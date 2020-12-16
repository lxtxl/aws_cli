#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-address-book.html
	delete-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-address-book.html
	get-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-address-book.html
	update-address-book : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-address-book.html
    """

    write_parameter("alexaforbusiness", "search-address-books")