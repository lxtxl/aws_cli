#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-execution-targets.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # association-id : The association ID that includes the execution for which you want to view details.
    # execution-id : The execution ID for which you want to view details.
    """

    execute_two_parameter("ssm", "describe-association-execution-targets", "association-id", "execution-id", parameter_display_string)