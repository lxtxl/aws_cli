#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-databases.html
if __name__ == '__main__':
    """
	create-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html
	delete-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database.html
	get-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html
	reboot-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-relational-database.html
	start-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-relational-database.html
	stop-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-relational-database.html
	update-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-relational-database.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("lightsail", "get-relational-databases", add_option_dict)