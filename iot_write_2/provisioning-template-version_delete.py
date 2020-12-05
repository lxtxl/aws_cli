#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template-version.html
if __name__ == '__main__':
    """
	create-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template-version.html
	describe-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template-version.html
	list-provisioning-template-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-template-versions.html
    """

    parameter_display_string = """
    # template-name : The name of the fleet provisioning template version to delete.
    # version-id : The fleet provisioning template version ID to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "delete-provisioning-template-version", "template-name", "version-id", add_option_dict)
