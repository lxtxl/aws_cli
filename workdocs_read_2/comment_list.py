#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-comments.html
if __name__ == '__main__':
    """
	create-comment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-comment.html
	delete-comment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-comment.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    # version-id : The ID of the document version.
    """

    execute_two_parameter("workdocs", "describe-comments", "document-id", "version-id", parameter_display_string)