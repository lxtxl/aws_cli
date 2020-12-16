#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/associate-team-member.html
if __name__ == '__main__':
    """
	disassociate-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/disassociate-team-member.html
	list-team-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-team-members.html
	update-team-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-team-member.html
    """

    parameter_display_string = """
    # project-id : The ID of the project to which you will add the IAM user.
    # user-arn : The Amazon Resource Name (ARN) for the IAM user you want to add to the AWS CodeStar project.
    # project-role : The AWS CodeStar project role that will apply to this user. This role determines what actions a user can take in an AWS CodeStar project.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codestar", "associate-team-member", "project-id", "user-arn", "project-role", add_option_dict)
