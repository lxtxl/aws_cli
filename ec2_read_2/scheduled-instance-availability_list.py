#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instance-availability.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # first-slot-start-time-range : 
    # recurrence : 
    """

    execute_two_parameter("ec2", "describe-scheduled-instance-availability", "first-slot-start-time-range", "recurrence", parameter_display_string)