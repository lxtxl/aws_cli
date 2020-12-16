#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template.html
if __name__ == '__main__':
    """
	delete-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template.html
	describe-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template.html
	list-provisioning-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-templates.html
	update-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-provisioning-template.html
    """

    parameter_display_string = """
    # template-name : The name of the fleet provisioning template.
    # template-body : The JSON formatted contents of the fleet provisioning template.
    # provisioning-role-arn : The role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot", "create-provisioning-template", "template-name", "template-body", "provisioning-role-arn", add_option_dict)
