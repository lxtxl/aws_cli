#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance.html
if __name__ == '__main__':
    """
	create-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance.html
	delete-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance.html
	list-app-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instances.html
	update-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-app-instance.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the app instance.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("chime", "describe-app-instance", "app-instance-arn", add_option_dict)