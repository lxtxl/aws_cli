#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html
if __name__ == '__main__':
    """
	create-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-document.html
	delete-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-document.html
	describe-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html
	get-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html
	list-documents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html
    """

    parameter_display_string = """
    # content : A valid JSON or YAML string.
    # name : The name of the document that you want to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "update-document", "content", "name", add_option_dict)
