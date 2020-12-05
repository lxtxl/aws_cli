#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-vtl-device-type.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # vtl-device-arn : The Amazon Resource Name (ARN) of the medium changer you want to select.
    # device-type : The type of medium changer you want to select.
Valid Values: STK-L700 | AWS-Gateway-VTL | IBM-03584L32-0402
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "update-vtl-device-type", "vtl-device-arn", "device-type", add_option_dict)
