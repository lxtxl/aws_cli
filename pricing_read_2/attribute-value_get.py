#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/get-attribute-values.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-code : The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use AmazonEC2 .
    # attribute-name : The name of the attribute that you want to retrieve the values for, such as volumeType .
    """

    execute_two_parameter("pricing", "get-attribute-values", "service-code", "attribute-name", parameter_display_string)