#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-discovered-resources.html
if __name__ == '__main__':
    """
	associate-discovered-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/associate-discovered-resource.html
	disassociate-discovered-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/disassociate-discovered-resource.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : The name of the MigrationTask. Do not store personal data in this field.
    """

    execute_two_parameter("mgh", "list-discovered-resources", "progress-update-stream", "migration-task-name", parameter_display_string)