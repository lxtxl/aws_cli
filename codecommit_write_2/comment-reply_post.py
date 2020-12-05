#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-reply.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # in-reply-to : The system-generated ID of the comment to which you want to reply. To get this ID, use  GetCommentsForComparedCommit or  GetCommentsForPullRequest .
    # content : The contents of your reply to a comment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codecommit", "post-comment-reply", "in-reply-to", "content", add_option_dict)
