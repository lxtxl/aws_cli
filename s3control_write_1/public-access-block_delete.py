#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-public-access-block.html
if __name__ == '__main__':
    """
	get-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-public-access-block.html
	put-public-access-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-public-access-block.html
    """

    parameter_display_string = """
    # account-id : The account ID for the AWS account whose PublicAccessBlock configuration you want to remove.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3control", "delete-public-access-block", "account-id", add_option_dict)





