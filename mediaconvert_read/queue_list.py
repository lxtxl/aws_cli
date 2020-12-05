#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html
	get-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-queue.html
	update-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("mediaconvert", "list-queues", add_option_dict)