#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/delete-server.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-server.html
	describe-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/describe-servers.html
	restore-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/restore-server.html
	update-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/update-server.html
    """

    parameter_display_string = """
    # server-name : The ID of the server to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks-cm", "delete-server", "server-name", add_option_dict)





