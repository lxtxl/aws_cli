#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html
if __name__ == '__main__':
    """
	delete-anomaly-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-anomaly-detector.html
	describe-anomaly-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-anomaly-detectors.html
    """

    parameter_display_string = """
    # namespace : The namespace of the metric to create the anomaly detection model for.
    # metric-name : The name of the metric to create the anomaly detection model for.
    # stat : The statistic to use for the metric and the anomaly detection model.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudwatch", "put-anomaly-detector", "namespace", "metric-name", "stat", add_option_dict)
