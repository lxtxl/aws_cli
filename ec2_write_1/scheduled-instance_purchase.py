#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-scheduled-instances.html
if __name__ == '__main__':
    """
	describe-scheduled-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instances.html
	run-scheduled-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html
    """

    parameter_display_string = """
    # purchase-requests : The purchase requests.
(structure)

Describes a request to purchase Scheduled Instances.
InstanceCount -> (integer)

The number of instances.

PurchaseToken -> (string)

The purchase token.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "purchase-scheduled-instances", "purchase-requests", add_option_dict)





