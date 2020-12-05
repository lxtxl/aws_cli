#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-test-grid-url.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # project-arn : ARN (from  CreateTestGridProject or  ListTestGridProjects ) to associate with the short-term URL.
    # expires-in-seconds : Lifetime, in seconds, of the URL.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("devicefarm", "create-test-grid-url", "project-arn", "expires-in-seconds", add_option_dict)
