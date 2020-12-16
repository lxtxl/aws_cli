#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html
if __name__ == '__main__':
    """
	create-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html
	delete-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-resource-data-sync.html
	list-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html
    """

    parameter_display_string = """
    # sync-name : The name of the resource data sync you want to update.
    # sync-type : The type of resource data sync. The supported SyncType is SyncFromSource.
    # sync-source : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ssm", "update-resource-data-sync", "sync-name", "sync-type", "sync-source", add_option_dict)
