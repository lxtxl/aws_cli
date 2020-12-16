#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-usage-forecast.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # time-period : 
    # metric : Which metric Cost Explorer uses to create your forecast.
Valid values for a GetUsageForecast call are the following:

USAGE_QUANTITY
NORMALIZED_USAGE_AMOUNT

Possible values:

BLENDED_COST
UNBLENDED_COST
AMORTIZED_COST
NET_UNBLENDED_COST
NET_AMORTIZED_COST
USAGE_QUANTITY
NORMALIZED_USAGE_AMOUNT
    """

    execute_two_parameter("ce", "get-usage-forecast", "time-period", "metric", parameter_display_string)