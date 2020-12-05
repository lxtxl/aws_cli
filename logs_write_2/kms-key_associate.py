#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/associate-kms-key.html
if __name__ == '__main__':
    """
	disassociate-kms-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/disassociate-kms-key.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # kms-key-id : The Amazon Resource Name (ARN) of the CMK to use when encrypting log data. This must be a symmetric CMK. For more information, see Amazon Resource Names - AWS Key Management Service (AWS KMS) and Using Symmetric and Asymmetric Keys .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "associate-kms-key", "log-group-name", "kms-key-id", add_option_dict)
