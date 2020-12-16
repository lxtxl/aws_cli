#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html
if __name__ == '__main__':
    """
	delete-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-branch.html
	get-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html
	list-branches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository in which you want to create the new branch.
    # branch-name : The name of the new branch to create.
    # commit-id : The ID of the commit to point the new branch to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codecommit", "create-branch", "repository-name", "branch-name", "commit-id", add_option_dict)
