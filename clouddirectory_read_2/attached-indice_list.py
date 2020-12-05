#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-attached-indices.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory.
    # target-reference : 
    """

    execute_two_parameter("clouddirectory", "list-attached-indices", "directory-arn", "target-reference", parameter_display_string)