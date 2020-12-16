#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # portfolio-id : The portfolio identifier.
    # principal-arn : The ARN of the principal (IAM user, role, or group).
    # principal-type : The principal type. The supported value is IAM .
Possible values:

IAM
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicecatalog", "associate-principal-with-portfolio", "portfolio-id", "principal-arn", "principal-type", add_option_dict)
