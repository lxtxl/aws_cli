#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html
if __name__ == '__main__':
    """
	create-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html
	delete-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-subnet-group.html
	modify-replication-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("dms", "describe-replication-subnet-groups", add_option_dict)