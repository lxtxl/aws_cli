#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-permission.html
if __name__ == '__main__':
    """
	put-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/put-permission.html
    """

    parameter_display_string = """
    # action-group : Specifies an action group that contains the permissions to remove from a profiling groupâs resource-based policy. One action group is supported, agentPermissions , which grants ConfigureAgent and PostAgentProfile permissions.
Possible values:

agentPermissions
    # profiling-group-name : The name of the profiling group.
    # revision-id : A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeguruprofiler", "remove-permission", "action-group", "profiling-group-name", "revision-id", add_option_dict)
