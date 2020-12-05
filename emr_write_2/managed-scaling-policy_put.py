#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/put-managed-scaling-policy.html
if __name__ == '__main__':
    """
	get-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-managed-scaling-policy.html
	remove-managed-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/remove-managed-scaling-policy.html
    """

    parameter_display_string = """
    # cluster-id : Specifies the ID of an EMR cluster where the managed scaling policy is attached.
    # managed-scaling-policy : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("emr", "put-managed-scaling-policy", "cluster-id", "managed-scaling-policy", add_option_dict)
