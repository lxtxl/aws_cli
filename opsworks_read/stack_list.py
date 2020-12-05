#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-stacks.html
if __name__ == '__main__':
    """
	clone-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/clone-stack.html
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-stack.html
	start-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-stack.html
	stop-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-stack.html
	update-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-stack.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("opsworks", "describe-stacks", add_option_dict)