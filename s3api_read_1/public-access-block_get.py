#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-public-access-block.html
if __name__ == '__main__':
    """
	delete-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-public-access-block.html
	put-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-public-access-block.html
    """

    parameter_display_string = """
    # bucket : The name of the Amazon S3 bucket whose PublicAccessBlock configuration you want to retrieve.
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

    read_one_parameter("s3api", "get-public-access-block", "bucket", add_option_dict)