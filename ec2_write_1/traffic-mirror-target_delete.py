#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-target.html
if __name__ == '__main__':
    """
	create-traffic-mirror-target : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-target.html
	describe-traffic-mirror-targets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-targets.html
    """

    parameter_display_string = """
    # traffic-mirror-target-id : The ID of the Traffic Mirror target.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-traffic-mirror-target", "traffic-mirror-target-id", add_option_dict)





