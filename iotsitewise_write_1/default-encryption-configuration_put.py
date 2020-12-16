#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/put-default-encryption-configuration.html
if __name__ == '__main__':
    """
	describe-default-encryption-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-default-encryption-configuration.html
    """

    parameter_display_string = """
    # encryption-type : The type of encryption used for the encryption configuration.
Possible values:

SITEWISE_DEFAULT_ENCRYPTION
KMS_BASED_ENCRYPTION
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "put-default-encryption-configuration", "encryption-type", add_option_dict)





