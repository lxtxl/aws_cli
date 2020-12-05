#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-tags.html
if __name__ == '__main__':
    """
	remove-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-tags.html
    """

    parameter_display_string = """
    # resource-id : The Amazon EMR resource identifier to which tags will be added. This value must be a cluster identifier.
    # tags : A list of tags to associate with a cluster, which apply to each Amazon EC2 instance in the cluster. Tags are key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
You can specify tags in key=value format or you can add a tag without a value using only the key name, for example key . Use a space to separate multiple tags.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "add-tags", "resource-id", "tags", add_option_dict)
