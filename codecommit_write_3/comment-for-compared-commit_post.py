#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-compared-commit.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository where you want to post a comment on the comparison between commits.
    # after-commit-id : To establish the directionality of the comparison, the full commit ID of the after commit.
    # content : The content of the comment you want to make.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codecommit", "post-comment-for-compared-commit", "repository-name", "after-commit-id", "content", add_option_dict)
