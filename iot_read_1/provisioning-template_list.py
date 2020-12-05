#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template.html
if __name__ == '__main__':
    """
	create-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template.html
	delete-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template.html
	list-provisioning-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-templates.html
	update-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-provisioning-template.html
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

    execute_one_parameter("iot", "describe-provisioning-template", "template-name", add_option_dict)