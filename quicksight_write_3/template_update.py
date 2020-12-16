#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template.html
if __name__ == '__main__':
    """
	create-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template.html
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-template.html
	describe-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-templates.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the template that youâre updating.
    # template-id : The ID for the template.
    # source-entity : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "update-template", "aws-account-id", "template-id", "source-entity", add_option_dict)
