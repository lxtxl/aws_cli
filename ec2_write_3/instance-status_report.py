#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html
if __name__ == '__main__':
    """
	describe-instance-status : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-status.html
    """

    parameter_display_string = """
    # instances : The instances.
(string)
    # reason-codes : The reason codes that describe the health state of your instance.

instance-stuck-in-state : My instance is stuck in a state.
unresponsive : My instance is unresponsive.
not-accepting-credentials : My instance is not accepting my credentials.
password-not-available : A password is not available for my instance.
performance-network : My instance is experiencing performance problems that I believe are network related.
performance-instance-store : My instance is experiencing performance problems that I believe are related to the instance stores.
performance-ebs-volume : My instance is experiencing performance problems that I believe are related to an EBS volume.
performance-other : My instance is experiencing performance problems.
other : [explain using the description parameter]

(string)
    # status : The status of all instances listed.
Possible values:

ok
impaired
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "report-instance-status", "instances", "reason-codes", "status", add_option_dict)
