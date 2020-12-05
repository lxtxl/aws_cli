#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-chap-credentials.html
if __name__ == '__main__':
    """
	delete-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-chap-credentials.html
	update-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-chap-credentials.html
    """

    parameter_display_string = """
    # target-arn : The Amazon Resource Name (ARN) of the iSCSI volume target. Use the  DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
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

    execute_one_parameter("storagegateway", "describe-chap-credentials", "target-arn", add_option_dict)