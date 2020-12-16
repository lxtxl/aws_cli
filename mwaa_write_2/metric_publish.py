#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/publish-metrics.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # environment-name : Publishes environment metric data to Amazon CloudWatch.
    # metric-data : Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metrica.
(structure)

Internal only API.
Dimensions -> (list)

Internal only API.
(structure)

Internal only API.
Name -> (string)

Internal only API.

Value -> (string)

Internal only API.



MetricName -> (string)

Internal only API.

StatisticValues -> (structure)

Internal only API.
Maximum -> (double)

Internal only API.

Minimum -> (double)

Internal only API.

SampleCount -> (integer)

Internal only API.

Sum -> (double)

Internal only API.


Timestamp -> (timestamp)

Internal only API.

Unit -> (string)

Unit

Value -> (double)

Internal only API.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mwaa", "publish-metrics", "environment-name", "metric-data", add_option_dict)
