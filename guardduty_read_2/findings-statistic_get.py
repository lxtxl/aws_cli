#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings-statistics.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # detector-id : The ID of the detector that specifies the GuardDuty service whose findingsâ statistics you want to retrieve.
    # finding-statistic-types : The types of finding statistics to retrieve.
(string)
    """

    execute_two_parameter("guardduty", "get-findings-statistics", "detector-id", "finding-statistic-types", parameter_display_string)