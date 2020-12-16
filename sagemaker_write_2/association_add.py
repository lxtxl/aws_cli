#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/add-association.html
if __name__ == '__main__':
    """
	delete-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-association.html
	list-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-associations.html
    """

    parameter_display_string = """
    # source-arn : The ARN of the source.
    # destination-arn : The Amazon Resource Name (ARN) of the destination.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "add-association", "source-arn", "destination-arn", add_option_dict)
