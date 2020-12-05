#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html
if __name__ == '__main__':
    """
	activate-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html
	deactivate-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/deactivate-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html
    """

    parameter_display_string = """
    # pipeline-ids : The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call  ListPipelines .
(string)
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

    execute_one_parameter("datapipeline", "describe-pipelines", "pipeline-ids", add_option_dict)