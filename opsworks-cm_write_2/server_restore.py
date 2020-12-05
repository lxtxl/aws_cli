#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/restore-server.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-server.html
	delete-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/delete-server.html
	describe-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/describe-servers.html
	update-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/update-server.html
    """

    parameter_display_string = """
    # backup-id : The ID of the backup that you want to use to restore a server.
    # server-name : The name of the server that you want to restore.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks-cm", "restore-server", "backup-id", "server-name", add_option_dict)
