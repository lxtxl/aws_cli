#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-automatic-tape-creation-policy.html
if __name__ == '__main__':
    """
	list-automatic-tape-creation-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-automatic-tape-creation-policies.html
	update-automatic-tape-creation-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-automatic-tape-creation-policy.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "delete-automatic-tape-creation-policy", "gateway-arn", add_option_dict)





