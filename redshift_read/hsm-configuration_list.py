#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-configurations.html
if __name__ == '__main__':
    """
	create-hsm-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-configuration.html
	delete-hsm-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("redshift", "describe-hsm-configurations", add_option_dict)