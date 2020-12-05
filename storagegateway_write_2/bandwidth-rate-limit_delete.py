#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-bandwidth-rate-limit.html
if __name__ == '__main__':
    """
	describe-bandwidth-rate-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-bandwidth-rate-limit.html
	update-bandwidth-rate-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-bandwidth-rate-limit.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # bandwidth-type : One of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.
Valid Values: UPLOAD | DOWNLOAD | ALL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "delete-bandwidth-rate-limit", "gateway-arn", "bandwidth-type", add_option_dict)
