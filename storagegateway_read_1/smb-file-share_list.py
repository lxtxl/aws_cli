#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-file-shares.html
if __name__ == '__main__':
    """
	create-smb-file-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-smb-file-share.html
	update-smb-file-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share.html
    """

    parameter_display_string = """
    # file-share-arn-list : An array containing the Amazon Resource Name (ARN) of each file share to be described.
(string)

The Amazon Resource Name (ARN) of the file share.
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

    execute_one_parameter("storagegateway", "describe-smb-file-shares", "file-share-arn-list", add_option_dict)