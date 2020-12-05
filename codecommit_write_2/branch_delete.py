#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-branch.html
if __name__ == '__main__':
    """
	create-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html
	get-branch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html
	list-branches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository that contains the branch to be deleted.
    # branch-name : The name of the branch to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "delete-branch", "repository-name", "branch-name", add_option_dict)
