#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html
if __name__ == '__main__':
    """
	delete-bucket-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-encryption.html
	put-bucket-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket from which the server-side encryption configuration is retrieved.
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

    read_one_parameter("s3api", "get-bucket-encryption", "bucket", add_option_dict)