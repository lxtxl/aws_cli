#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/tag-resource.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html
    """

    parameter_display_string = """
    # organization-id : The identifier associated with the organization for which the resource is updated.
    # resource-id : The identifier of the resource to be updated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "update-resource", "organization-id", "resource-id", add_option_dict)
