#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-auto-scaling-policy.html
if __name__ == '__main__':
    """
	remove-auto-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-auto-scaling-policy.html
    """

    parameter_display_string = """
    # cluster-id : Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.
    # instance-group-id : Specifies the ID of the instance group to which the automatic scaling policy is applied.
    # auto-scaling-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("emr", "put-auto-scaling-policy", "cluster-id", "instance-group-id", "auto-scaling-policy", add_option_dict)
