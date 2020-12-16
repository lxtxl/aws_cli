#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/get-config.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # client-arn : The ARN of the client.
    # client-version : The client version.
Possible values:

5.1
5.3
    """

    execute_two_parameter("cloudhsm", "get-config", "client-arn", "client-version", parameter_display_string)