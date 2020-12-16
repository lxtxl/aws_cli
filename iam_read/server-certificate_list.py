#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificates.html
if __name__ == '__main__':
    """
	delete-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-server-certificate.html
	get-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-server-certificate.html
	update-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-server-certificate.html
	upload-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-server-certificate.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iam", "list-server-certificates", add_option_dict)