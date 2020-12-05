#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-phone-number-order.html
if __name__ == '__main__':
    """
	get-phone-number-order : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number-order.html
	list-phone-number-orders : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-number-orders.html
    """

    parameter_display_string = """
    # product-type : The phone number product type.
Possible values:

BusinessCalling
VoiceConnector
    # e164-phone-numbers : List of phone numbers, in E.164 format.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "create-phone-number-order", "product-type", "e164-phone-numbers", add_option_dict)
