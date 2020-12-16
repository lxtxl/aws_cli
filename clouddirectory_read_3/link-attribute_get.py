#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-link-attributes.html
if __name__ == '__main__':
    """
	update-link-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-link-attributes.html
    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see  arns or Typed Links .
    # typed-link-specifier : 
    """

    execute_two_parameter("clouddirectory", "get-link-attributes", "directory-arn", "typed-link-specifier", parameter_display_string)