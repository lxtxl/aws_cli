#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template.html
if __name__ == '__main__':
    """
	create-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template.html
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-templates.html
	update-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the template that youâre describing.
    # template-id : The ID for the template.
    """

    execute_two_parameter("quicksight", "describe-template", "aws-account-id", "template-id", parameter_display_string)