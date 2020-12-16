#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/put-permission.html
if __name__ == '__main__':
    """
	remove-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-permission.html
    """

    parameter_display_string = """
    # action-group : Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, agentPermissions , which grants permission to perform actions required by the profiling agent, ConfigureAgent and PostAgentProfile permissions.
Possible values:

agentPermissions
    # principals : A list ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not are supported in the ARNs.
(string)
    # profiling-group-name : The name of the profiling group to grant access to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codeguruprofiler", "put-permission", "action-group", "principals", "profiling-group-name", add_option_dict)
