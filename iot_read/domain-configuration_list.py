#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-domain-configurations.html
if __name__ == '__main__':
    """
	create-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-domain-configuration.html
	delete-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-domain-configuration.html
	describe-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html
	update-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-domain-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iot", "list-domain-configurations", add_option_dict)