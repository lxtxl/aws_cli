#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-instance-profile.html
if __name__ == '__main__':
    """
	create-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-instance-profile.html
	delete-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-instance-profile.html
	get-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-instance-profile.html
	list-instance-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-instance-profiles.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the instance profile.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "update-instance-profile", "arn", add_option_dict)





