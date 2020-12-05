#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html
if __name__ == '__main__':
    """
	create-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html
	get-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html
	list-access-points : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html
    """

    parameter_display_string = """
    # account-id : The account ID for the account that owns the specified access point.
    # name : The name of the access point you want to delete.
For Amazon S3 on Outposts specify the ARN of the access point accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name> . For example, to access the access point reports-ap through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap . The value must be URL encoded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3control", "delete-access-point", "account-id", "name", add_option_dict)
