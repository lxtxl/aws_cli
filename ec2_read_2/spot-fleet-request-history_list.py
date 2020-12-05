#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-request-history.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # spot-fleet-request-id : The ID of the Spot Fleet request.
    # start-time : 
    """

    execute_two_parameter("ec2", "describe-spot-fleet-request-history", "spot-fleet-request-id", "start-time", parameter_display_string)