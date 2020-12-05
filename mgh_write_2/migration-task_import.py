#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/import-migration-task.html
if __name__ == '__main__':
    """
	describe-migration-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/describe-migration-task.html
	list-migration-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-migration-tasks.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream. >
    # migration-task-name : Unique identifier that references the migration task. Do not store personal data in this field.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mgh", "import-migration-task", "progress-update-stream", "migration-task-name", add_option_dict)
