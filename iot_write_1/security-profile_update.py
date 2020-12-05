#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-security-profile.html
if __name__ == '__main__':
    """
	attach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-security-profile.html
	create-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html
	delete-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-security-profile.html
	describe-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-security-profile.html
	detach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-security-profile.html
	list-security-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles.html
    """

    parameter_display_string = """
    # security-profile-name : The name of the security profile you want to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "update-security-profile", "security-profile-name", add_option_dict)





