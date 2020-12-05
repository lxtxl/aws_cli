#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-team-members.html
if __name__ == '__main__':
    """
	associate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/associate-team-member.html
	disassociate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/disassociate-team-member.html
	update-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-team-member.html
    """

    parameter_display_string = """
    # project-id : The ID of the project for which you want to list team members.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("codestar", "list-team-members", "project-id", add_option_dict)