#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-contact-attributes.html
if __name__ == '__main__':
    """
	update-contact-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-attributes.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # initial-contact-id : The identifier of the initial contact.
    """

    execute_two_parameter("connect", "get-contact-attributes", "instance-id", "initial-contact-id", parameter_display_string)