#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment.html
if __name__ == '__main__':
    """
	update-comment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-comment.html
    """

    parameter_display_string = """
    # comment-id : The unique, system-generated ID of the comment. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
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

    execute_one_parameter("codecommit", "get-comment", "comment-id", add_option_dict)