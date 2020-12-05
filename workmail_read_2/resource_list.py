#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/tag-resource.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html
    """

    parameter_display_string = """
    # organization-id : The identifier associated with the organization for which the resource is described.
    # resource-id : The identifier of the resource to be described.
    """

    execute_two_parameter("workmail", "describe-resource", "organization-id", "resource-id", parameter_display_string)