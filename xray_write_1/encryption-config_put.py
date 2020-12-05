#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-encryption-config.html
if __name__ == '__main__':
    """
	get-encryption-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-encryption-config.html
    """

    parameter_display_string = """
    # type : The type of encryption. Set to KMS to use your own key for encryption. Set to NONE for default encryption.
Possible values:

NONE
KMS
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("xray", "put-encryption-config", "type", add_option_dict)





