#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-comment.html
if __name__ == '__main__':
    """
	get-comment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment.html
    """

    parameter_display_string = """
    # comment-id : The system-generated ID of the comment you want to update. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
    # content : The updated content to replace the existing content of the comment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "update-comment", "comment-id", "content", add_option_dict)
