#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-tags.html
if __name__ == '__main__':
    """
	create-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-tags.html
    """

    parameter_display_string = """
    # resource-name : The Amazon Resource Name (ARN) from which you want to remove the tag or tags. For example, arn:aws:redshift:us-east-2:123456789:cluster:t1 .
    # tag-keys : The tag key that you want to delete.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "delete-tags", "resource-name", "tag-keys", add_option_dict)
