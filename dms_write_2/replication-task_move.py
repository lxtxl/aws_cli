#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/move-replication-task.html
if __name__ == '__main__':
    """
	create-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html
	delete-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task.html
	describe-replication-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-tasks.html
	modify-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-task.html
	start-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task.html
	stop-replication-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html
    """

    parameter_display_string = """
    # replication-task-arn : The Amazon Resource Name (ARN) of the task that you want to move.
    # target-replication-instance-arn : The ARN of the replication instance where you want to move the task to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "move-replication-task", "replication-task-arn", "target-replication-instance-arn", add_option_dict)
