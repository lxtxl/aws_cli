#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-managed-scaling-policy.html
if __name__ == '__main__':
    """
	get-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-managed-scaling-policy.html
	put-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-managed-scaling-policy.html
    """

    parameter_display_string = """
    # cluster-id : Specifies the ID of the cluster from which the managed scaling policy will be removed.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("emr", "remove-managed-scaling-policy", "cluster-id", add_option_dict)





