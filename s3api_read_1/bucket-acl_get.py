#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-acl.html
if __name__ == '__main__':
    """
	put-bucket-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-acl.html
    """

    parameter_display_string = """
    # bucket : Specifies the S3 bucket whose ACL is being requested.
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

    read_one_parameter("s3api", "get-bucket-acl", "bucket", add_option_dict)