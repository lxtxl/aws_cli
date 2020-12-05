#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-pipeline.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-pipelines.html
	update-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-pipeline.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline whose information is retrieved.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iotanalytics", "describe-pipeline", "pipeline-name", add_option_dict)