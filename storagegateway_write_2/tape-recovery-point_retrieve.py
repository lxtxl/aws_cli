#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/retrieve-tape-recovery-point.html
if __name__ == '__main__':
    """
	describe-tape-recovery-points : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tape-recovery-points.html
    """

    parameter_display_string = """
    # tape-arn : The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "retrieve-tape-recovery-point", "tape-arn", "gateway-arn", add_option_dict)
