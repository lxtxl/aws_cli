#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-nfs-file-share.html
if __name__ == '__main__':
    """
	create-nfs-file-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-nfs-file-share.html
	describe-nfs-file-shares : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-nfs-file-shares.html
    """

    parameter_display_string = """
    # file-share-arn : The Amazon Resource Name (ARN) of the file share to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "update-nfs-file-share", "file-share-arn", add_option_dict)





