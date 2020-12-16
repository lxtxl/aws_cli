#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html
if __name__ == '__main__':
    """
	create-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-document.html
	delete-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-document.html
	describe-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html
	get-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html
	update-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ssm", "list-documents", add_option_dict)