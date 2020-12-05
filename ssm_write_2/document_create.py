#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-document.html
if __name__ == '__main__':
    """
	delete-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-document.html
	describe-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html
	get-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html
	list-documents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html
	update-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html
    """

    parameter_display_string = """
    # content : The content for the new SSM document in JSON or YAML format. We recommend storing the contents for your new document in an external JSON or YAML file and referencing the file in a command.
For examples, see the following topics in the AWS Systems Manager User Guide .

Create an SSM document (AWS API)
Create an SSM document (AWS CLI)
Create an SSM document (API)
    # name : A name for the Systems Manager document.

Warning
You canât use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:

aws-
amazon
amzn
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "create-document", "content", "name", add_option_dict)
