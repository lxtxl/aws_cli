#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-index.html
if __name__ == '__main__':
    """
	create-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-index.html
    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory that the index exists in.
    # index-reference : 
    """

    execute_two_parameter("clouddirectory", "list-index", "directory-arn", "index-reference", parameter_display_string)