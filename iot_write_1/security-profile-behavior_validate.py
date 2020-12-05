#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/validate-security-profile-behaviors.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # behaviors : Specifies the behaviors that, when violated by a device (thing), cause an alert.
(structure)

A Device Defender security profile behavior.
name -> (string)

The name you have given to the behavior.

metric -> (string)

What is measured by the behavior.

metricDimension -> (structure)

The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.
dimensionName -> (string)

A unique identifier for the dimension.

operator -> (string)

Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesnât match any of the topic filters. The operator is optional: if itâs not provided (is null ), it will be interpreted as IN .


criteria -> (structure)

The criteria that determine if a device is behaving normally in regard to the metric .
comparisonOperator -> (string)

The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).

value -> (structure)

The value to be compared with the metric .
count -> (long)

If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs -> (list)

If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .
(string)

ports -> (list)

If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .
(integer)


durationSeconds -> (integer)

Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.

consecutiveDatapointsToAlarm -> (integer)

If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear -> (integer)

If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold -> (structure)

A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
statistic -> (string)

The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "validate-security-profile-behaviors", "behaviors", add_option_dict)





