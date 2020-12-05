#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-subnet-group.html
if __name__ == '__main__':
    """
	create-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html
	describe-replication-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html
	modify-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html
    """

    parameter_display_string = """
    # replication-subnet-group-identifier : The subnet group name of the replication instance.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "delete-replication-subnet-group", "replication-subnet-group-identifier", add_option_dict)





