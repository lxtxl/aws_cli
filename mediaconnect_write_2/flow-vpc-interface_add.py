#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-vpc-interfaces.html
if __name__ == '__main__':
    """
	remove-flow-vpc-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-vpc-interface.html
    """

    parameter_display_string = """
    # flow-arn : The flow that you want to mutate.
    # vpc-interfaces : Desired VPC Interface for a Flow
Name -> (string)

The name of the VPC Interface. This value must be unique within the current flow.

RoleArn -> (string)

Role Arn MediaConnect can assumes to create ENIs in customerâs account

SecurityGroupIds -> (list)

Security Group IDs to be used on ENI.
(string)

SubnetId -> (string)

Subnet must be in the AZ of the Flow
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "add-flow-vpc-interfaces", "flow-arn", "vpc-interfaces", add_option_dict)
