#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/disassociate-trial-component.html
if __name__ == '__main__':
    """
	associate-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/associate-trial-component.html
	create-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial-component.html
	delete-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-trial-component.html
	describe-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial-component.html
	list-trial-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-trial-components.html
	update-trial-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-trial-component.html
    """

    parameter_display_string = """
    # trial-component-name : The name of the component to disassociate from the trial.
    # trial-name : The name of the trial to disassociate from.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "disassociate-trial-component", "trial-component-name", "trial-name", add_option_dict)
