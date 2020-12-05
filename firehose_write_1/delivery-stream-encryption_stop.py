#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/stop-delivery-stream-encryption.html
if __name__ == '__main__':
    """
	start-delivery-stream-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/start-delivery-stream-encryption.html
    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream for which you want to disable server-side encryption (SSE).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("firehose", "stop-delivery-stream-encryption", "delivery-stream-name", add_option_dict)





