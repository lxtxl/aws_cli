#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-instance-access.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # fleet-id : A unique identifier for a fleet that contains the instance you want access to. You can use either the fleet ID or ARN value. The fleet can be in any of the following statuses: ACTIVATING , ACTIVE , or ERROR . Fleets with an ERROR status may be accessible for a short time before they are deleted.
    # instance-id : A unique identifier for an instance you want to get access to. You can access an instance in any status.
    """

    execute_two_parameter("gamelift", "get-instance-access", "fleet-id", "instance-id", parameter_display_string)