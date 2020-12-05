#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-object-parents.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory where the object resides. For more information, see  arns .
    # object-reference : 
    """

    execute_two_parameter("clouddirectory", "list-object-parents", "directory-arn", "object-reference", parameter_display_string)