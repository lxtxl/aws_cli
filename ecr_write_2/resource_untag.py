#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository.
    # tag-keys : The keys of the tags to be removed.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
