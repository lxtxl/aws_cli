#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share.html
if __name__ == '__main__':
    """
	create-smb-file-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-smb-file-share.html
	describe-smb-file-shares : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-file-shares.html
    """

    parameter_display_string = """
    # file-share-arn : The Amazon Resource Name (ARN) of the SMB file share that you want to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "update-smb-file-share", "file-share-arn", add_option_dict)





