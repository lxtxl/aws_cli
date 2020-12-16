#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html
if __name__ == '__main__':
    """
	delete-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-subnet-group.html
	describe-replication-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html
	modify-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html
    """

    parameter_display_string = """
    # replication-subnet-group-identifier : The name for the replication subnet group. This value is stored as a lowercase string.
Constraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores, or hyphens. Must not be âdefaultâ.
Example: mySubnetgroup
    # replication-subnet-group-description : The description for the subnet group.
    # subnet-ids : One or more subnet IDs to be assigned to the subnet group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dms", "create-replication-subnet-group", "replication-subnet-group-identifier", "replication-subnet-group-description", "subnet-ids", add_option_dict)
