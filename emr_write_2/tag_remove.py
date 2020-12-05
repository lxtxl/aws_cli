#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-tags.html
if __name__ == '__main__':
    """
	add-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/add-tags.html
    """

    parameter_display_string = """
    # resource-id : The Amazon EMR resource identifier from which tags will be removed. This value must be a cluster identifier.
    # tag-keys : A list of tag keys to remove from a resource.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "remove-tags", "resource-id", "tag-keys", add_option_dict)
