#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-subnet-group.html
if __name__ == '__main__':
    """
	delete-cluster-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-subnet-group.html
	describe-cluster-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-subnet-groups.html
	modify-cluster-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-subnet-group.html
    """

    parameter_display_string = """
    # cluster-subnet-group-name : The name for the subnet group. Amazon Redshift stores the value as a lowercase string.
Constraints:

Must contain no more than 255 alphanumeric characters or hyphens.
Must not be âDefaultâ.
Must be unique for all subnet groups that are created by your AWS account.

Example: examplesubnetgroup
    # description : A description for the subnet group.
    # subnet-ids : An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("redshift", "create-cluster-subnet-group", "cluster-subnet-group-name", "description", "subnet-ids", add_option_dict)
