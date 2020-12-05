#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-created-artifacts.html
if __name__ == '__main__':
    """
	associate-created-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/associate-created-artifact.html
	disassociate-created-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/disassociate-created-artifact.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : Unique identifier that references the migration task. Do not store personal data in this field.
    """

    execute_two_parameter("mgh", "list-created-artifacts", "progress-update-stream", "migration-task-name", parameter_display_string)