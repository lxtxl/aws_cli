#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-data-source.html
if __name__ == '__main__':
    """
	create-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-data-source.html
	describe-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-data-source.html
	list-data-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-data-sources.html
	update-data-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-source.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID.
    # data-source-id : The ID of the data source. This ID is unique per AWS Region for each AWS account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "delete-data-source", "aws-account-id", "data-source-id", add_option_dict)
