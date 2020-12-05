#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html
if __name__ == '__main__':
    """
	create-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html
	migrate-workspace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/migrate-workspace.html
	reboot-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/reboot-workspaces.html
	rebuild-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/rebuild-workspaces.html
	restore-workspace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/restore-workspace.html
	start-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/start-workspaces.html
	stop-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/stop-workspaces.html
	terminate-workspaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/terminate-workspaces.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("workspaces", "describe-workspaces", add_option_dict)