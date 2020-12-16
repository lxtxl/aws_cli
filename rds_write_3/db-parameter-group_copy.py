#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-parameter-group.html
if __name__ == '__main__':
    """
	create-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-parameter-group.html
	delete-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-parameter-group.html
	describe-db-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-parameter-groups.html
	modify-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html
	reset-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-parameter-group.html
    """

    parameter_display_string = """
    # source-db-parameter-group-identifier : The identifier or ARN for the source DB parameter group. For information about creating an ARN, see Constructing an ARN for Amazon RDS in the Amazon RDS User Guide .
Constraints:

Must specify a valid DB parameter group.
Must specify a valid DB parameter group identifier, for example my-db-param-group , or a valid ARN.
    # target-db-parameter-group-identifier : The identifier for the copied DB parameter group.
Constraints:

Canât be null, empty, or blank
Must contain from 1 to 255 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens

Example: my-db-parameter-group
    # target-db-parameter-group-description : A description for the copied DB parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "copy-db-parameter-group", "source-db-parameter-group-identifier", "target-db-parameter-group-identifier", "target-db-parameter-group-description", add_option_dict)
