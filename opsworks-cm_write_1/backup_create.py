#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-backup.html
if __name__ == '__main__':
    """
	delete-backup : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/delete-backup.html
	describe-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/describe-backups.html
    """

    parameter_display_string = """
    # server-name : The name of the server that you want to back up.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("opsworks-cm", "create-backup", "server-name", add_option_dict)





