#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-chap-credentials.html
if __name__ == '__main__':
    """
	describe-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-chap-credentials.html
	update-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-chap-credentials.html
    """

    parameter_display_string = """
    # target-arn : The Amazon Resource Name (ARN) of the iSCSI volume target. Use the  DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
    # initiator-name : The iSCSI initiator that connects to the target.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "delete-chap-credentials", "target-arn", "initiator-name", add_option_dict)
