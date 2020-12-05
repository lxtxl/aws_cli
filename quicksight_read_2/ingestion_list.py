#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-ingestions.html
if __name__ == '__main__':
    """
	cancel-ingestion : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/cancel-ingestion.html
	create-ingestion : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-ingestion.html
	describe-ingestion : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-ingestion.html
    """

    parameter_display_string = """
    # data-set-id : The ID of the dataset used in the ingestion.
    # aws-account-id : The AWS account ID.
    """

    execute_two_parameter("quicksight", "list-ingestions", "data-set-id", "aws-account-id", parameter_display_string)