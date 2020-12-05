#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/describe-migration-task.html
if __name__ == '__main__':
    """
	import-migration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/import-migration-task.html
	list-migration-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-migration-tasks.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : The identifier given to the MigrationTask. Do not store personal data in this field.
    """

    execute_two_parameter("mgh", "describe-migration-task", "progress-update-stream", "migration-task-name", parameter_display_string)