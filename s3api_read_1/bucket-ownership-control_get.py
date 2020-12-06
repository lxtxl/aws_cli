#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-ownership-controls.html
if __name__ == '__main__':
    """
	delete-bucket-ownership-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-ownership-controls.html
	put-bucket-ownership-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html
    """

    parameter_display_string = """
    # bucket : The name of the Amazon S3 bucket whose OwnershipControls you want to retrieve.
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

    read_one_parameter("s3api", "get-bucket-ownership-controls", "bucket", add_option_dict)