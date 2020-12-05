#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleet-history.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # fleet-id : The ID of the EC2 Fleet.
    # start-time : 
    """

    execute_two_parameter("ec2", "describe-fleet-history", "fleet-id", "start-time", parameter_display_string)