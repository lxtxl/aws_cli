#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployment-groups.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-name : The name of an AWS CodeDeploy application associated with the applicable IAM user or AWS account.
    # deployment-group-names : The names of the deployment groups.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("deploy", "batch-get-deployment-groups", "application-name", "deployment-group-names", add_option_dict)
