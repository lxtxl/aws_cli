#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    # stack-name : This property corresponds to the parameter of the same name for the *AWS CloudFormation CreateChangeSet * API.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("serverlessrepo", "create-cloud-formation-change-set", "application-id", "stack-name", add_option_dict)
