#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html
if __name__ == '__main__':
    """
	attach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html
	create-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html
	delete-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk.html
	detach-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-disk.html
	get-disk : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("lightsail", "get-disks", add_option_dict)