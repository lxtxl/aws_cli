#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-kms-encryption-key.html
if __name__ == '__main__':
    """
	get-kms-encryption-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-kms-encryption-key.html
    """

    parameter_display_string = """
    # kms-encryption-key-arn : The KMS encryption key ARN.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "put-kms-encryption-key", "kms-encryption-key-arn", add_option_dict)





