#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-public-access-block.html
if __name__ == '__main__':
    """
	delete-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-public-access-block.html
	get-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-public-access-block.html
    """

    parameter_display_string = """
    # public-access-block-configuration : 
    # account-id : The account ID for the AWS account whose PublicAccessBlock configuration you want to set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3control", "put-public-access-block", "public-access-block-configuration", "account-id", add_option_dict)
