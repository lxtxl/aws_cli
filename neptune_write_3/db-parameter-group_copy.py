#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-parameter-group.html
if __name__ == '__main__':
    """
	create-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-parameter-group.html
	delete-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-parameter-group.html
	describe-db-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-parameter-groups.html
	modify-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-parameter-group.html
	reset-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reset-db-parameter-group.html
    """

    parameter_display_string = """
    # source-db-parameter-group-identifier : The identifier or ARN for the source DB parameter group. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
Constraints:

Must specify a valid DB parameter group.
Must specify a valid DB parameter group identifier, for example my-db-param-group , or a valid ARN.
    # target-db-parameter-group-identifier : The identifier for the copied DB parameter group.
Constraints:

Cannot be null, empty, or blank.
Must contain from 1 to 255 letters, numbers, or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: my-db-parameter-group
    # target-db-parameter-group-description : A description for the copied DB parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("neptune", "copy-db-parameter-group", "source-db-parameter-group-identifier", "target-db-parameter-group-identifier", "target-db-parameter-group-description", add_option_dict)
