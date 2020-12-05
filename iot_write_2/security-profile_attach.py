#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-security-profile.html
if __name__ == '__main__':
    """
	create-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html
	delete-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-security-profile.html
	describe-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-security-profile.html
	detach-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-security-profile.html
	list-security-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles.html
	update-security-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-security-profile.html
    """

    parameter_display_string = """
    # security-profile-name : The security profile that is attached.
    # security-profile-target-arn : The ARN of the target (thing group) to which the security profile is attached.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "attach-security-profile", "security-profile-name", "security-profile-target-arn", add_option_dict)
