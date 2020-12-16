#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/disassociate-created-artifact.html
if __name__ == '__main__':
    """
	associate-created-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/associate-created-artifact.html
	list-created-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-created-artifacts.html
    """

    parameter_display_string = """
    # progress-update-stream : The name of the ProgressUpdateStream.
    # migration-task-name : Unique identifier that references the migration task to be disassociated with the artifact. Do not store personal data in this field.
    # created-artifact-name : An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mgh", "disassociate-created-artifact", "progress-update-stream", "migration-task-name", "created-artifact-name", add_option_dict)
