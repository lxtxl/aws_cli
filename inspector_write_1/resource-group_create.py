#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-resource-group.html
if __name__ == '__main__':
    """
	describe-resource-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-resource-groups.html
    """

    parameter_display_string = """
    # resource-group-tags : A collection of keys and an array of possible values, â[{âkeyâ:âkey1â,âvaluesâ:[âValue1â,âValue2â]},{âkeyâ:âKey2â,âvaluesâ:[âValue3â]}]â.
For example,â[{âkeyâ:âNameâ,âvaluesâ:[âTestEC2Instanceâ]}]â.
(structure)

This data type is used as one of the elements of the  ResourceGroup data type.
key -> (string)

A tag key.

value -> (string)

The value assigned to a tag key.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("inspector", "create-resource-group", "resource-group-tags", add_option_dict)





