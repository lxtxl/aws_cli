#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
if __name__ == '__main__':
    """
	delete-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html
	update-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html
	upload-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iam", "list-signing-certificates", add_option_dict)