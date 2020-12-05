#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/list-directories.html
if __name__ == '__main__':
    """
	create-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-directory.html
	disable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/disable-directory.html
	enable-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/enable-directory.html
	get-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/get-directory.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("clouddirectory", "list-directories", add_option_dict)