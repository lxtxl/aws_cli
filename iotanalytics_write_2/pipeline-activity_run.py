#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/run-pipeline-activity.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pipeline-activity : 
    # payloads : The sample message payloads on which the pipeline activity is run.
(blob)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotanalytics", "run-pipeline-activity", "pipeline-activity", "payloads", add_option_dict)
