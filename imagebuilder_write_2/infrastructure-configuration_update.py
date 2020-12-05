#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html
if __name__ == '__main__':
    """
	create-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-infrastructure-configuration.html
	delete-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-infrastructure-configuration.html
	get-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-infrastructure-configuration.html
	list-infrastructure-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-infrastructure-configurations.html
    """

    parameter_display_string = """
    # infrastructure-configuration-arn : The Amazon Resource Name (ARN) of the infrastructure configuration that you want to update.
    # instance-profile-name : The instance profile to associate with the instance used to customize your EC2 AMI.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("imagebuilder", "update-infrastructure-configuration", "infrastructure-configuration-arn", "instance-profile-name", add_option_dict)
