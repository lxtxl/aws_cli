#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-profile.html
if __name__ == '__main__':
    """
	delete-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-field-level-encryption-profile.html
	get-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-profile.html
	list-field-level-encryption-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-field-level-encryption-profiles.html
	update-field-level-encryption-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-field-level-encryption-profile.html
    """

    parameter_display_string = """
    # field-level-encryption-profile-config : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "create-field-level-encryption-profile", "field-level-encryption-profile-config", add_option_dict)





