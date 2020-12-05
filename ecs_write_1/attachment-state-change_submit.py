#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/submit-attachment-state-changes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # attachments : Any attachments associated with the state change request.
(structure)

An object representing a change in state for a task attachment.
attachmentArn -> (string)

The Amazon Resource Name (ARN) of the attachment.

status -> (string)

The status of the attachment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "submit-attachment-state-changes", "attachments", add_option_dict)





