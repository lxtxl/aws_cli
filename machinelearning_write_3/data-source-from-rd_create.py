#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-rds.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # data-source-id : A user-supplied ID that uniquely identifies the DataSource . Typically, an Amazon Resource Number (ARN) becomes the ID for a DataSource .
    # rds-data : 
    # role-arn : The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the userâs account and copy data using the SelectSqlQuery query from Amazon RDS to Amazon S3.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "create-data-source-from-rds", "data-source-id", "rds-data", "role-arn", add_option_dict)
