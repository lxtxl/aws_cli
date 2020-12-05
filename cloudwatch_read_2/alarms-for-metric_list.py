#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarms-for-metric.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # metric-name : The name of the metric.
    # namespace : The namespace of the metric.
    """

    execute_two_parameter("cloudwatch", "describe-alarms-for-metric", "metric-name", "namespace", parameter_display_string)