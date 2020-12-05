#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html
if __name__ == '__main__':
    """
	modify-document-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html
    """

    parameter_display_string = """
    # name : The name of the document for which you are the owner.
    # permission-type : The permission type for the document. The permission type can be Share .
Possible values:

Share
    """

    execute_two_parameter("ssm", "describe-document-permission", "name", "permission-type", parameter_display_string)