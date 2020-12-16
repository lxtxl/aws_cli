#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshots.html
if __name__ == '__main__':
    """
	create-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database-snapshot.html
	delete-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database-snapshot.html
	get-relational-database-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshot.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("lightsail", "get-relational-database-snapshots", add_option_dict)