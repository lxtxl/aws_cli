#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	create-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-parameter-groups.html
	modify-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-parameter-group.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # source-db-cluster-parameter-group-identifier : The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see Constructing an ARN for Amazon RDS in the Amazon Aurora User Guide .
Constraints:

Must specify a valid DB cluster parameter group.
If the source DB cluster parameter group is in the same AWS Region as the copy, specify a valid DB parameter group identifier, for example my-db-cluster-param-group , or a valid ARN.
If the source DB parameter group is in a different AWS Region than the copy, specify a valid DB cluster parameter group ARN, for example arn:aws:rds:us-east-1:123456789012:cluster-pg:custom-cluster-group1 .
    # target-db-cluster-parameter-group-identifier : The identifier for the copied DB cluster parameter group.
Constraints:

Canât be null, empty, or blank
Must contain from 1 to 255 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-cluster-param-group1
    # target-db-cluster-parameter-group-description : A description for the copied DB cluster parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "copy-db-cluster-parameter-group", "source-db-cluster-parameter-group-identifier", "target-db-cluster-parameter-group-identifier", "target-db-cluster-parameter-group-description", add_option_dict)
