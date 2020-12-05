#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-reserved-instances.html
if __name__ == '__main__':
    """
	describe-reserved-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances.html
    """

    parameter_display_string = """
    # reserved-instances-ids : The IDs of the Reserved Instances to modify.
(string)
    # target-configurations : The configuration settings for the Reserved Instances to modify.
(structure)

Describes the configuration settings for the modified Reserved Instances.
AvailabilityZone -> (string)

The Availability Zone for the modified Reserved Instances.

InstanceCount -> (integer)

The number of modified Reserved Instances.

Note
This is a required field for a request.


InstanceType -> (string)

The instance type for the modified Reserved Instances.

Platform -> (string)

The network platform of the modified Reserved Instances, which is either EC2-Classic or EC2-VPC.

Scope -> (string)

Whether the Reserved Instance is applied to instances in a Region or instances in a specific Availability Zone.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "modify-reserved-instances", "reserved-instances-ids", "target-configurations", add_option_dict)
