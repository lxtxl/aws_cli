#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template-alias.html
if __name__ == '__main__':
    """
	create-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template-alias.html
	delete-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-template-alias.html
	update-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template-alias.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the template alias that youâre describing.
    # template-id : The ID for the template.
    """

    execute_two_parameter("quicksight", "describe-template-alias", "aws-account-id", "template-id", parameter_display_string)