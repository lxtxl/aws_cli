#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/render-ui-template.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # task : 
    # role-arn : The Amazon Resource Name (ARN) that has access to the S3 objects that are used by the template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "render-ui-template", "task", "role-arn", add_option_dict)
