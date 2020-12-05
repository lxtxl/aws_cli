#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-legal-hold.html
if __name__ == '__main__':
    """
	get-object-legal-hold : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-legal-hold.html
    """

    parameter_display_string = """
    # bucket : The bucket name containing the object that you want to place a Legal Hold on.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
    # key : The key name for the object that you want to place a Legal Hold on.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-object-legal-hold", "bucket", "key", add_option_dict)
