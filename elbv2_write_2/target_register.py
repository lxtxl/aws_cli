#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/register-targets.html
if __name__ == '__main__':
    """
	deregister-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/deregister-targets.html
    """

    parameter_display_string = """
    # target-group-arn : The Amazon Resource Name (ARN) of the target group.
    # targets : The targets.
(structure)

Information about a target.
Id -> (string)

The ID of the target. If the target type of the target group is instance , specify an instance ID. If the target type is ip , specify an IP address. If the target type is lambda , specify the ARN of the Lambda function.

Port -> (integer)

The port on which the target is listening. If the target group protocol is GENEVE, the supported port is 6081. Not used if the target is a Lambda function.

AvailabilityZone -> (string)

An Availability Zone or all . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
This parameter is not supported if the target type of the target group is instance .
If the target type is ip and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
With an Application Load Balancer, if the target type is ip and the IP address is outside the VPC for the target group, the only supported value is all .
If the target type is lambda , this parameter is optional and the only supported value is all .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "register-targets", "target-group-arn", "targets", add_option_dict)
