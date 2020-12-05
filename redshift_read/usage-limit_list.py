#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-usage-limits.html
if __name__ == '__main__':
    """
	create-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-usage-limit.html
	delete-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-usage-limit.html
	modify-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-usage-limit.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("redshift", "describe-usage-limits", add_option_dict)