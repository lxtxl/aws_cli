#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/commit-transaction.html
if __name__ == '__main__':
    """
	begin-transaction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/begin-transaction.html
	rollback-transaction : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/rollback-transaction.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
    # secret-arn : The name or ARN of the secret that enables access to the DB cluster.
    # transaction-id : The identifier of the transaction to end and commit.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds-data", "commit-transaction", "resource-arn", "secret-arn", "transaction-id", add_option_dict)
