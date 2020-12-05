#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html
if __name__ == '__main__':
    """
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/delete-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group.html
    """

    parameter_display_string = """
    # name : The name of the group, which is the identifier of the group in other operations. You canât change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with AWS or aws ; these are reserved. A resource group name must be unique within each AWS Region in your AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("resource-groups", "create-group", "name", add_option_dict)





