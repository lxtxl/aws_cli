#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-and-usage.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # time-period : 
    # metrics : Which metrics are returned in the query. For more information about blended and unblended rates, see Why does the âblendedâ annotation appear on some line items in my bill? .
Valid values are AmortizedCost , BlendedCost , NetAmortizedCost , NetUnblendedCost , NormalizedUsageAmount , UnblendedCost , and UsageQuantity .

Note

If you return the UsageQuantity metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate usageQuantity across all of Amazon EC2, the results arenât meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful UsageQuantity metrics, filter by UsageType or UsageTypeGroups .

Metrics is required for GetCostAndUsage requests.

(string)
    """

    execute_two_parameter("ce", "get-cost-and-usage", "time-period", "metrics", parameter_display_string)