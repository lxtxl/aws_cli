#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-use-cases.html
if __name__ == '__main__':
    """
	create-use-case : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-use-case.html
	delete-use-case : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-use-case.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # integration-association-id : The identifier for the integration association.
    """

    execute_two_parameter("connect", "list-use-cases", "instance-id", "integration-association-id", parameter_display_string)