#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-infrastructure-configurations.html
if __name__ == '__main__':
    """
	create-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-infrastructure-configuration.html
	delete-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-infrastructure-configuration.html
	get-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-infrastructure-configuration.html
	update-infrastructure-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("imagebuilder", "list-infrastructure-configurations", add_option_dict)