#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-artifacts.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # arn : The run, job, suite, or test ARN.
    # type : The artifactsâ type.
Allowed values include:

FILE
LOG
SCREENSHOT

Possible values:

SCREENSHOT
FILE
LOG
    """

    execute_two_parameter("devicefarm", "list-artifacts", "arn", "type", parameter_display_string)