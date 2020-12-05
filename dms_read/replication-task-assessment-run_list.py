#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-task-assessment-runs.html
if __name__ == '__main__':
    """
	cancel-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/cancel-replication-task-assessment-run.html
	delete-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task-assessment-run.html
	start-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task-assessment-run.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("dms", "describe-replication-task-assessment-runs", add_option_dict)