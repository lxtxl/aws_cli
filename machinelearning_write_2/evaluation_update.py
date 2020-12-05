#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-evaluation.html
if __name__ == '__main__':
    """
	create-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-evaluation.html
	delete-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-evaluation.html
	describe-evaluations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-evaluations.html
	get-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-evaluation.html
    """

    parameter_display_string = """
    # evaluation-id : The ID assigned to the Evaluation during creation.
    # evaluation-name : A new user-supplied name or description of the Evaluation that will replace the current content.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("machinelearning", "update-evaluation", "evaluation-id", "evaluation-name", add_option_dict)
