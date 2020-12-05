#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/complete-migration.html
if __name__ == '__main__':
    """
	start-migration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/start-migration.html
    """

    parameter_display_string = """
    # replication-group-id : The ID of the replication group to which data is being migrated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "complete-migration", "replication-group-id", add_option_dict)





