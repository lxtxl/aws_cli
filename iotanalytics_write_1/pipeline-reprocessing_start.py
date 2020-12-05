#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/start-pipeline-reprocessing.html
if __name__ == '__main__':
    """
	cancel-pipeline-reprocessing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/cancel-pipeline-reprocessing.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline on which to start reprocessing.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotanalytics", "start-pipeline-reprocessing", "pipeline-name", add_option_dict)





