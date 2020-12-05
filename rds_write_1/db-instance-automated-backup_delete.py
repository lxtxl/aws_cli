#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance-automated-backup.html
if __name__ == '__main__':
    """
	describe-db-instance-automated-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instance-automated-backups.html
    """

    parameter_display_string = """
    # dbi-resource-id : The identifier for the source DB instance, which canât be changed and which is unique to an AWS Region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-db-instance-automated-backup", "dbi-resource-id", add_option_dict)





