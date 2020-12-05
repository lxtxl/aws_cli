#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-deployment-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # deployment-id : The ID of the deployment.
    # group-id : The ID of the Greengrass group.
    """

    execute_two_parameter("greengrass", "get-deployment-status", "deployment-id", "group-id", parameter_display_string)