#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/tag-resource.html
    """

    parameter_display_string = """
    # resource-name : The name of the DAX resource from which the tags should be removed.
    # tag-keys : A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dax", "untag-resource", "resource-name", "tag-keys", add_option_dict)
