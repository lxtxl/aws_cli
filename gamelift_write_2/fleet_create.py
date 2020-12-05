#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html
if __name__ == '__main__':
    """
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-fleet.html
	list-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-fleets.html
    """

    parameter_display_string = """
    # name : A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
    # ec2-instance-type : The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
Possible values:

t2.micro
t2.small
t2.medium
t2.large
c3.large
c3.xlarge
c3.2xlarge
c3.4xlarge
c3.8xlarge
c4.large
c4.xlarge
c4.2xlarge
c4.4xlarge
c4.8xlarge
c5.large
c5.xlarge
c5.2xlarge
c5.4xlarge
c5.9xlarge
c5.12xlarge
c5.18xlarge
c5.24xlarge
r3.large
r3.xlarge
r3.2xlarge
r3.4xlarge
r3.8xlarge
r4.large
r4.xlarge
r4.2xlarge
r4.4xlarge
r4.8xlarge
r4.16xlarge
r5.large
r5.xlarge
r5.2xlarge
r5.4xlarge
r5.8xlarge
r5.12xlarge
r5.16xlarge
r5.24xlarge
m3.medium
m3.large
m3.xlarge
m3.2xlarge
m4.large
m4.xlarge
m4.2xlarge
m4.4xlarge
m4.10xlarge
m5.large
m5.xlarge
m5.2xlarge
m5.4xlarge
m5.8xlarge
m5.12xlarge
m5.16xlarge
m5.24xlarge
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "create-fleet", "name", "ec2-instance-type", add_option_dict)
