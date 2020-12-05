#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/untag-resource.html
    """

    parameter_display_string = """
    # resource-id : The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use  DescribeClusters .
    # tag-list : A list of one or more tags.
(structure)

Contains a tag. A tag is a key-value pair.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "tag-resource", "resource-id", "tag-list", add_option_dict)
