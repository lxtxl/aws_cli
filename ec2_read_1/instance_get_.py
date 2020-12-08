#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	bundle-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/bundle-instance.html
	monitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/monitor-instances.html
	reboot-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reboot-instances.html
	run-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html
	start-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-instances.html
	stop-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html
	terminate-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html
	unmonitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unmonitor-instances.html
    """

    parameter_display_string = """
        instance-ids : instance id
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    read_one_parameter("ec2", "describe-instances", "instance-ids", add_option_dict)