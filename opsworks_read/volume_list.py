#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-volumes.html
if __name__ == '__main__':
    """
	assign-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-volume.html
	deregister-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-volume.html
	register-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-volume.html
	unassign-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-volume.html
	update-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-volume.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("opsworks", "describe-volumes", add_option_dict)