#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # alarm-name : The name for the alarm. This name must be unique within the Region.
    # evaluation-periods : The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an âM out of Nâ alarm, this value is the N.
An alarmâs total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.
    # comparison-operator : The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
The values LessThanLowerOrGreaterThanUpperThreshold , LessThanLowerThreshold , and GreaterThanUpperThreshold are used only for alarms based on anomaly detection models.
Possible values:

GreaterThanOrEqualToThreshold
GreaterThanThreshold
LessThanThreshold
LessThanOrEqualToThreshold
LessThanLowerOrGreaterThanUpperThreshold
LessThanLowerThreshold
GreaterThanUpperThreshold
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudwatch", "put-metric-alarm", "alarm-name", "evaluation-periods", "comparison-operator", add_option_dict)
