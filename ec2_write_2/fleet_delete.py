#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-fleets.html
if __name__ == '__main__':
    """
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html
	describe-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleets.html
	modify-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-fleet.html
    """

    parameter_display_string = """
    # fleet-ids : The IDs of the EC2 Fleets.
(string)
    # terminate-instances | --no-terminate-instances : Indicates whether to terminate instances for an EC2 Fleet if it is deleted successfully.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "delete-fleets", "fleet-ids", "terminate-instances | --no-terminate-instances", add_option_dict)
