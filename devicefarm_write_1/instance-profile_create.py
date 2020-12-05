#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-instance-profile.html
if __name__ == '__main__':
    """
	delete-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-instance-profile.html
	get-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-instance-profile.html
	list-instance-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-instance-profiles.html
	update-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-instance-profile.html
    """

    parameter_display_string = """
    # name : The name of your instance profile.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "create-instance-profile", "name", add_option_dict)





