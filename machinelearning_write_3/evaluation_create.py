#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-evaluation.html
if __name__ == '__main__':
    """
	delete-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-evaluation.html
	describe-evaluations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-evaluations.html
	get-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-evaluation.html
	update-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-evaluation.html
    """

    parameter_display_string = """
    # evaluation-id : A user-supplied ID that uniquely identifies the Evaluation .
    # ml-model-id : The ID of the MLModel to evaluate.
The schema used in creating the MLModel must match the schema of the DataSource used in the Evaluation .
    # evaluation-data-source-id : The ID of the DataSource for the evaluation. The schema of the DataSource must match the schema used to create the MLModel .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "create-evaluation", "evaluation-id", "ml-model-id", "evaluation-data-source-id", add_option_dict)
