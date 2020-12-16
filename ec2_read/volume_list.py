#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html
if __name__ == '__main__':
    """
	attach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html
	create-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html
	delete-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-volume.html
	detach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-volume.html
	modify-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ec2", "describe-volumes", add_option_dict)