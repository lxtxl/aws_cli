#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-policy-attachments.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory where objects reside. For more information, see  arns .
    # policy-reference : 
    """

    execute_two_parameter("clouddirectory", "list-policy-attachments", "directory-arn", "policy-reference", parameter_display_string)