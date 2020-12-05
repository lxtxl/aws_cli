#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape.html
if __name__ == '__main__':
    """
	create-tapes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tapes.html
	describe-tapes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tapes.html
	list-tapes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tapes.html
    """

    parameter_display_string = """
    # gateway-arn : The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # tape-arn : The Amazon Resource Name (ARN) of the virtual tape to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "delete-tape", "gateway-arn", "tape-arn", add_option_dict)
