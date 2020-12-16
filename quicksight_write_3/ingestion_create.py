#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-ingestion.html
if __name__ == '__main__':
    """
	cancel-ingestion : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/cancel-ingestion.html
	describe-ingestion : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-ingestion.html
	list-ingestions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-ingestions.html
    """

    parameter_display_string = """
    # data-set-id : The ID of the dataset used in the ingestion.
    # ingestion-id : An ID for the ingestion.
    # aws-account-id : The AWS account ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "create-ingestion", "data-set-id", "ingestion-id", "aws-account-id", add_option_dict)
