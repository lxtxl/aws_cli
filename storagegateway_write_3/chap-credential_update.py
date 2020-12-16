#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-chap-credentials.html
if __name__ == '__main__':
    """
	delete-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-chap-credentials.html
	describe-chap-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-chap-credentials.html
    """

    parameter_display_string = """
    # target-arn : The Amazon Resource Name (ARN) of the iSCSI volume target. Use the  DescribeStorediSCSIVolumes operation to return the TargetARN for specified VolumeARN.
    # secret-to-authenticate-initiator : The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.

Note
The secret key must be between 12 and 16 bytes when encoded in UTF-8.
    # initiator-name : The iSCSI initiator that connects to the target.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("storagegateway", "update-chap-credentials", "target-arn", "secret-to-authenticate-initiator", "initiator-name", add_option_dict)
