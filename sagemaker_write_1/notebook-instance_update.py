#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html
if __name__ == '__main__':
    """
	create-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance.html
	delete-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-notebook-instance.html
	describe-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance.html
	list-notebook-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instances.html
	start-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-notebook-instance.html
	stop-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-notebook-instance.html
    """

    parameter_display_string = """
    # notebook-instance-name : The name of the notebook instance to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "update-notebook-instance", "notebook-instance-name", add_option_dict)





