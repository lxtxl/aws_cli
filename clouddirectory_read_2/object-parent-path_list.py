#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-object-parent-paths.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The ARN of the directory to which the parent path applies.
    # object-reference : 
    """

    execute_two_parameter("clouddirectory", "list-object-parent-paths", "directory-arn", "object-reference", parameter_display_string)