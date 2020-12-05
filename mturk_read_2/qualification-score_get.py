#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-score.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # qualification-type-id : The ID of the QualificationType.
    # worker-id : The ID of the Worker whose Qualification is being updated.
    """

    execute_two_parameter("mturk", "get-qualification-score", "qualification-type-id", "worker-id", parameter_display_string)