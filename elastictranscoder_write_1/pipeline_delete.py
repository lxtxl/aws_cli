#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/delete-pipeline.html
if __name__ == '__main__':
    """
	create-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/create-pipeline.html
	list-pipelines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-pipelines.html
	read-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-pipeline.html
	update-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/update-pipeline.html
    """

    parameter_display_string = """
    # id : The identifier of the pipeline that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elastictranscoder", "delete-pipeline", "id", add_option_dict)





