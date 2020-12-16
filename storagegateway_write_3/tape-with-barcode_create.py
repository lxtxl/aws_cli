#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-with-barcode.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # gateway-arn : The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # tape-size-in-bytes : 
    # tape-barcode : The barcode that you want to assign to the tape.

Note
Barcodes cannot be reused. This includes barcodes used for tapes that have been deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("storagegateway", "create-tape-with-barcode", "gateway-arn", "tape-size-in-bytes", "tape-barcode", add_option_dict)
