#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html
if __name__ == '__main__':
    """
	delete-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html
	describe-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html
	modify-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html
	reset-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html
    """

    parameter_display_string = """
    # parameter-group-name : The name of the cluster parameter group.
Constraints:

Must be 1 to 255 alphanumeric characters or hyphens
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
Must be unique withing your AWS account.


Note
This value is stored as a lower-case string.
    # parameter-group-family : The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.
To get a list of valid parameter group family names, you can call  DescribeClusterParameterGroups . By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is âredshift-1.0â.
    # description : A description of the parameter group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("redshift", "create-cluster-parameter-group", "parameter-group-name", "parameter-group-family", "description", add_option_dict)
