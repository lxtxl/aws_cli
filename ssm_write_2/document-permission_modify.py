#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html
if __name__ == '__main__':
    """
	describe-document-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html
    """

    parameter_display_string = """
    # name : The name of the document that you want to share.
    # permission-type : The permission type for the document. The permission type can be Share .
Possible values:

Share
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "modify-document-permission", "name", "permission-type", add_option_dict)
