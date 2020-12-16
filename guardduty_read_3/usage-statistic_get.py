#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-usage-statistics.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # detector-id : The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.
    # usage-statistic-type : The type of usage statistics to retrieve.
Possible values:

SUM_BY_ACCOUNT
SUM_BY_DATA_SOURCE
SUM_BY_RESOURCE
TOP_RESOURCES
    """

    execute_two_parameter("guardduty", "get-usage-statistics", "detector-id", "usage-statistic-type", parameter_display_string)