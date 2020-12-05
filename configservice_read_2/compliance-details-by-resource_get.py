#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-type : The type of the AWS resource for which you want compliance information.
    # resource-id : The ID of the AWS resource for which you want compliance information.
    """

    execute_two_parameter("configservice", "get-compliance-details-by-resource", "resource-type", "resource-id", parameter_display_string)