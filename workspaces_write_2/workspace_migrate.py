#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/migrate-workspace.html
if __name__ == '__main__':
    """
	create-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html
	describe-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html
	reboot-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/reboot-workspaces.html
	rebuild-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/rebuild-workspaces.html
	restore-workspace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/restore-workspace.html
	start-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/start-workspaces.html
	stop-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/stop-workspaces.html
	terminate-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/terminate-workspaces.html
    """

    parameter_display_string = """
    # source-workspace-id : The identifier of the WorkSpace to migrate from.
    # bundle-id : The identifier of the target bundle type to migrate the WorkSpace to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "migrate-workspace", "source-workspace-id", "bundle-id", add_option_dict)
