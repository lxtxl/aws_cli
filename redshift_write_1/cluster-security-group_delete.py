#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-security-group.html
if __name__ == '__main__':
    """
	create-cluster-security-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html
	describe-cluster-security-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-security-groups.html
    """

    parameter_display_string = """
    # cluster-security-group-name : The name of the cluster security group to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "delete-cluster-security-group", "cluster-security-group-name", add_option_dict)





