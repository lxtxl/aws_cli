#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template.html
if __name__ == '__main__':
    """
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-template.html
	describe-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-templates.html
	update-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # template-id : An ID for the template that you want to create. This template is unique per AWS Region in each AWS account.
    # source-entity : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "create-template", "aws-account-id", "template-id", "source-entity", add_option_dict)
