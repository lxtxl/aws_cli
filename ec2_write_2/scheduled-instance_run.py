#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html
if __name__ == '__main__':
    """
	describe-scheduled-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instances.html
	purchase-scheduled-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-scheduled-instances.html
    """

    parameter_display_string = """
    # launch-specification : 
    # scheduled-instance-id : The Scheduled Instance ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "run-scheduled-instances", "launch-specification", "scheduled-instance-id", add_option_dict)
