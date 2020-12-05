#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html
if __name__ == '__main__':
    """
	delete-cluster-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-security-group.html
	describe-cluster-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-security-groups.html
    """

    parameter_display_string = """
    # cluster-security-group-name : The name for the security group. Amazon Redshift stores the value as a lowercase string.
Constraints:

Must contain no more than 255 alphanumeric characters or hyphens.
Must not be âDefaultâ.
Must be unique for all security groups that are created by your AWS account.

Example: examplesecuritygroup
    # description : A description for the security group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "create-cluster-security-group", "cluster-security-group-name", "description", add_option_dict)
