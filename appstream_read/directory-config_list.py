#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-directory-configs.html
if __name__ == '__main__':
    """
	create-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-directory-config.html
	delete-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-directory-config.html
	update-directory-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-directory-config.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("appstream", "describe-directory-configs", add_option_dict)