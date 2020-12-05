#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html
if __name__ == '__main__':
    """
	create-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html
	delete-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database.html
	get-relational-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-databases.html
	reboot-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-relational-database.html
	start-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-relational-database.html
	stop-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-relational-database.html
	update-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-relational-database.html
    """

    parameter_display_string = """
    # relational-database-name : The name of the database that you are looking up.
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

    execute_one_parameter("lightsail", "get-relational-database", "relational-database-name", add_option_dict)