#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-instance-profile.html
if __name__ == '__main__':
    """
	create-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-instance-profile.html
	get-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-instance-profile.html
	list-instance-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profiles.html
    """

    parameter_display_string = """
    # instance-profile-name : The name of the instance profile to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-instance-profile", "instance-profile-name", add_option_dict)





