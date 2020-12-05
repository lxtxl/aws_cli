#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-contact-flow.html
if __name__ == '__main__':
    """
	create-contact-flow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-contact-flow.html
	list-contact-flows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-contact-flows.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # contact-flow-id : The identifier of the contact flow.
    """

    execute_two_parameter("connect", "describe-contact-flow", "instance-id", "contact-flow-id", parameter_display_string)