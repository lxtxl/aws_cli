#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html
if __name__ == '__main__':
    """
	create-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/create-model.html
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-models.html
	start-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model.html
	stop-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/stop-model.html
    """

    parameter_display_string = """
    # project-name : The project that contains the version of a model that you want to describe.
    # model-version : The version of the model that you want to describe.
    """

    execute_two_parameter("lookoutvision", "describe-model", "project-name", "model-version", parameter_display_string)