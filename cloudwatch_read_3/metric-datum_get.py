#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-data.html
if __name__ == '__main__':
    """
	put-metric-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-data.html
    """

    parameter_display_string = """
    # metric-data-queries : The metric queries to be returned. A single GetMetricData call can include as many as 500 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.
(structure)

This structure is used in both GetMetricData and PutMetricAlarm . The supported use of this structure is different for those two operations.
When used in GetMetricData , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data. A single GetMetricData call can include up to 500 MetricDataQuery structures.
When used in PutMetricAlarm , it enables you to create an alarm based on a metric math expression. Each MetricDataQuery in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single PutMetricAlarm call can include up to 20 MetricDataQuery structures in the array. The 20 structures can include as many as 10 structures that contain a MetricStat parameter to retrieve a metric, and as many as 10 structures that contain the Expression parameter to perform a math expression. Of those Expression structures, one must have True as the value for ReturnData . The result of this expression is the value the alarm watches.
Any expression used in a PutMetricAlarm operation must return a single time series. For more information, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Some of the parameters of this structure also have different uses whether you are using this structure in a GetMetricData operation or a PutMetricAlarm operation. These differences are explained in the following parameter list.
Id -> (string)

A short name used to tie this object to the results in the response. This name must be unique within a single call to GetMetricData . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

MetricStat -> (structure)

The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
Within one MetricDataQuery object, you must specify either Expression or MetricStat but not both.
Metric -> (structure)

The metric to return, including the metric name, namespace, and dimensions.
Namespace -> (string)

The namespace of the metric.

MetricName -> (string)

The name of the metric. This is a required field.

Dimensions -> (list)

The dimensions for the metric.
(structure)

A dimension is a name/value pair that is part of the identity of a metric. You can assign up to 10 dimensions to a metric. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric.
Name -> (string)

The name of the dimension. Dimension names cannot contain blank spaces or non-ASCII characters.

Value -> (string)

The value of the dimension. Dimension values cannot contain blank spaces or non-ASCII characters.




Period -> (integer)

The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second.
If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).


Stat -> (string)

The statistic to return. It can include any CloudWatch statistic or extended statistic.

Unit -> (string)

When you are using a Put operation, this defines what unit you want to use when storing the metric.
In a Get operation, if you omit Unit then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.


Expression -> (string)

The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the Id of the other metrics to refer to those metrics, and can also use the Id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide .
Within each MetricDataQuery object, you must specify either Expression or MetricStat but not both.

Label -> (string)

A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

ReturnData -> (boolean)

When used in GetMetricData , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False . If you omit this, the default of True is used.
When used in PutMetricAlarm , specify True for the one expression result to use as the alarm. For all other metrics and expressions in the same PutMetricAlarm operation, specify ReturnData as False.

Period -> (integer)

The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData operation that includes a StorageResolution of 1 second .
    # start-time : Specifies that log files delivered on or after the specified UTC timestamp value will be validated. Example: â2015-01-08T05:21:42Zâ.
    """

    execute_two_parameter("cloudwatch", "get-metric-data", "metric-data-queries", "start-time", parameter_display_string)