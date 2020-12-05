#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html
if __name__ == '__main__':
    """
	bundle-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/bundle-instance.html
	describe-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
	monitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/monitor-instances.html
	reboot-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reboot-instances.html
	run-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html
	start-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-instances.html
	terminate-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html
	unmonitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unmonitor-instances.html
    """

    parameter_display_string = """
    # instance-ids : The IDs of the instances.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "stop-instances", "instance-ids", add_option_dict)





