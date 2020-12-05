#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-team-member.html
if __name__ == '__main__':
    """
	associate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/associate-team-member.html
	disassociate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/disassociate-team-member.html
	list-team-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-team-members.html
    """

    parameter_display_string = """
    # project-id : The ID of the project.
    # user-arn : The Amazon Resource Name (ARN) of the user for whom you want to change team membership attributes.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codestar", "update-team-member", "project-id", "user-arn", add_option_dict)
