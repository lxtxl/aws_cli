#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/tag-resource.html
    """

    parameter_display_string = """
    # resource-id : The cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use  DescribeClusters .
    # tag-key-list : A list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "untag-resource", "resource-id", "tag-key-list", add_option_dict)
