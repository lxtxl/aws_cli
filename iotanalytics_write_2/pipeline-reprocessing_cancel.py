#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/cancel-pipeline-reprocessing.html
if __name__ == '__main__':
    """
	start-pipeline-reprocessing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/start-pipeline-reprocessing.html
    """

    parameter_display_string = """
    # pipeline-name : The name of pipeline for which data reprocessing is canceled.
    # reprocessing-id : The ID of the reprocessing task (returned by StartPipelineReprocessing ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotanalytics", "cancel-pipeline-reprocessing", "pipeline-name", "reprocessing-id", add_option_dict)
