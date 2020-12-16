#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # data-source-id : A user-supplied ID that uniquely identifies the DataSource .
    # data-spec : 
    # role-arn : A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:

A security group to allow Amazon ML to execute the SelectSqlQuery query on an Amazon Redshift cluster
An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the S3StagingLocation
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "create-data-source-from-redshift", "data-source-id", "data-spec", "role-arn", add_option_dict)
