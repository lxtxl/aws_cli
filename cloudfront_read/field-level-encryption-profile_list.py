#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-field-level-encryption-profiles.html
if __name__ == '__main__':
    """
	create-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-profile.html
	delete-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-field-level-encryption-profile.html
	get-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-profile.html
	update-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-field-level-encryption-profile.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("cloudfront", "list-field-level-encryption-profiles", add_option_dict)