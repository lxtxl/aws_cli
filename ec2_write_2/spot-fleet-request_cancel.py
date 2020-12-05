#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-fleet-requests.html
if __name__ == '__main__':
    """
	describe-spot-fleet-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-requests.html
	modify-spot-fleet-request : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-spot-fleet-request.html
    """

    parameter_display_string = """
    # spot-fleet-request-ids : The IDs of the Spot Fleet requests.
(string)
    # terminate-instances | --no-terminate-instances : Indicates whether to terminate instances for a Spot Fleet request if it is canceled successfully.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "cancel-spot-fleet-requests", "spot-fleet-request-ids", "terminate-instances | --no-terminate-instances", add_option_dict)
