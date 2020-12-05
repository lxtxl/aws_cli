#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-evaluation.html
if __name__ == '__main__':
    """
	create-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-evaluation.html
	describe-evaluations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-evaluations.html
	get-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-evaluation.html
	update-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-evaluation.html
    """

    parameter_display_string = """
    # evaluation-id : A user-supplied ID that uniquely identifies the Evaluation to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("machinelearning", "delete-evaluation", "evaluation-id", add_option_dict)





