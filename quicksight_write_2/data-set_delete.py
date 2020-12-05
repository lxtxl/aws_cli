#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-data-set.html
if __name__ == '__main__':
    """
	create-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-data-set.html
	describe-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-data-set.html
	list-data-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-data-sets.html
	update-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID.
    # data-set-id : The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "delete-data-set", "aws-account-id", "data-set-id", add_option_dict)
