#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html
if __name__ == '__main__':
    """
	assign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-instance.html
	create-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html
	delete-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-instance.html
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-instance.html
	reboot-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/reboot-instance.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html
	start-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-instance.html
	stop-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-instance.html
	unassign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-instance.html
	update-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-instance.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("opsworks", "describe-instances", add_option_dict)