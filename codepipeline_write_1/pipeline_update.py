#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/update-pipeline.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html
	delete-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-pipeline.html
	get-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipelines.html
    """

    parameter_display_string = """
    # pipeline : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codepipeline", "update-pipeline", "pipeline", add_option_dict)





