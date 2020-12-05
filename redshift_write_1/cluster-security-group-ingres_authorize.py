#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-cluster-security-group-ingress.html
if __name__ == '__main__':
    """
	revoke-cluster-security-group-ingress : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-cluster-security-group-ingress.html
    """

    parameter_display_string = """
    # cluster-security-group-name : The name of the security group to which the ingress rule is added.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "authorize-cluster-security-group-ingress", "cluster-security-group-name", add_option_dict)





