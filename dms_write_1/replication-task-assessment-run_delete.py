#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task-assessment-run.html
if __name__ == '__main__':
    """
	cancel-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/cancel-replication-task-assessment-run.html
	describe-replication-task-assessment-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-task-assessment-runs.html
	start-replication-task-assessment-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task-assessment-run.html
    """

    parameter_display_string = """
    # replication-task-assessment-run-arn : Amazon Resource Name (ARN) of the premigration assessment run to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "delete-replication-task-assessment-run", "replication-task-assessment-run-arn", add_option_dict)





