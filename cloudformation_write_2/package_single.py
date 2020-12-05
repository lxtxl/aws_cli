#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/package.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # template-file : The path where your AWS CloudFormation template is located.
    # s3-bucket : The name of the S3 bucket where this command uploads the artifacts that are referenced in your template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "package", "template-file", "s3-bucket", add_option_dict)
