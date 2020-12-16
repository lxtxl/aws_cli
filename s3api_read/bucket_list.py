#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html
if __name__ == '__main__':
    """
	create-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html
	delete-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html
	head-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("s3api", "list-buckets", add_option_dict)