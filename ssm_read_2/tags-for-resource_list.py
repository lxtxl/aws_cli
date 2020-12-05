#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-type : Returns a list of tags for a specific resource type.
Possible values:

Document
ManagedInstance
MaintenanceWindow
Parameter
PatchBaseline
OpsItem
    # resource-id : The resource ID for which you want to see a list of tags.
    """

    execute_two_parameter("ssm", "list-tags-for-resource", "resource-type", "resource-id", parameter_display_string)