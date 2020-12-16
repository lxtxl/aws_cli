#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-anomaly-detector.html
if __name__ == '__main__':
    """
	describe-anomaly-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-anomaly-detectors.html
	put-anomaly-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html
    """

    parameter_display_string = """
    # namespace : The namespace associated with the anomaly detection model to delete.
    # metric-name : The metric name associated with the anomaly detection model to delete.
    # stat : The statistic associated with the anomaly detection model to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudwatch", "delete-anomaly-detector", "namespace", "metric-name", "stat", add_option_dict)
