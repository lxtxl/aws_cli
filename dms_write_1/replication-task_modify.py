#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-task.html
if __name__ == '__main__':
    """
	create-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html
	delete-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task.html
	describe-replication-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-tasks.html
	start-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task.html
	stop-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html
    """

    parameter_display_string = """
    # replication-task-arn : The Amazon Resource Name (ARN) of the replication task.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "modify-replication-task", "replication-task-arn", add_option_dict)





