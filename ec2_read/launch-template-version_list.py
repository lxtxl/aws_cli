#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html
if __name__ == '__main__':
    """
	create-launch-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html
	delete-launch-template-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-launch-template-versions.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ec2", "describe-launch-template-versions", add_option_dict)