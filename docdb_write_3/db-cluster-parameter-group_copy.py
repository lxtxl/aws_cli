#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	create-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-parameter-groups.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # source-db-cluster-parameter-group-identifier : The identifier or Amazon Resource Name (ARN) for the source cluster parameter group.
Constraints:

Must specify a valid cluster parameter group.
If the source cluster parameter group is in the same AWS Region as the copy, specify a valid parameter group identifier; for example, my-db-cluster-param-group , or a valid ARN.
If the source parameter group is in a different AWS Region than the copy, specify a valid cluster parameter group ARN; for example, arn:aws:rds:us-east-1:123456789012:sample-cluster:sample-parameter-group .
    # target-db-cluster-parameter-group-identifier : The identifier for the copied cluster parameter group.
Constraints:

Cannot be null, empty, or blank.
Must contain from 1 to 255 letters, numbers, or hyphens.
The first character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-cluster-param-group1
    # target-db-cluster-parameter-group-description : A description for the copied cluster parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("docdb", "copy-db-cluster-parameter-group", "source-db-cluster-parameter-group-identifier", "target-db-cluster-parameter-group-identifier", "target-db-cluster-parameter-group-description", add_option_dict)
