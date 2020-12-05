#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-deployable-patch-snapshot-for-instance.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The ID of the instance for which the appropriate patch snapshot should be retrieved.
    # snapshot-id : The user-defined snapshot ID.
    """

    execute_two_parameter("ssm", "get-deployable-patch-snapshot-for-instance", "instance-id", "snapshot-id", parameter_display_string)