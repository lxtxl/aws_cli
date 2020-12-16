#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-comment.html
if __name__ == '__main__':
    """
	create-comment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-comment.html
	describe-comments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-comments.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    # version-id : The ID of the document version.
    # comment-id : The ID of the comment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("workdocs", "delete-comment", "document-id", "version-id", "comment-id", add_option_dict)
