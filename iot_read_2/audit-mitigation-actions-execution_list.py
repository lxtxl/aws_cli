#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-mitigation-actions-executions.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # task-id : Specify this filter to limit results to actions for a specific audit mitigation actions task.
    # finding-id : Specify this filter to limit results to those that were applied to a specific audit finding.
    """

    execute_two_parameter("iot", "list-audit-mitigation-actions-executions", "task-id", "finding-id", parameter_display_string)