#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-template-versions.html
if __name__ == '__main__':
    """
	create-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template-version.html
	delete-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template-version.html
	describe-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template-version.html
    """

    parameter_display_string = """
    # template-name : The name of the fleet provisioning template.
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

    execute_one_parameter("iot", "list-provisioning-template-versions", "template-name", add_option_dict)