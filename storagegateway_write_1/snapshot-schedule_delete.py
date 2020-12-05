#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-snapshot-schedule.html
if __name__ == '__main__':
    """
	describe-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-snapshot-schedule.html
	update-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-snapshot-schedule.html
    """

    parameter_display_string = """
    # volume-arn : The volume which snapshot schedule to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "delete-snapshot-schedule", "volume-arn", add_option_dict)





