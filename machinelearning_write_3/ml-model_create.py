#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-ml-model.html
if __name__ == '__main__':
    """
	delete-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-ml-model.html
	describe-ml-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-ml-models.html
	get-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-ml-model.html
	update-ml-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-ml-model.html
    """

    parameter_display_string = """
    # ml-model-id : A user-supplied ID that uniquely identifies the MLModel .
    # ml-model-type : The category of supervised learning that this MLModel will address. Choose from the following types:

Choose REGRESSION if the MLModel will be used to predict a numeric value.
Choose BINARY if the MLModel result has two possible values.
Choose MULTICLASS if the MLModel result has a limited number of values.

For more information, see the Amazon Machine Learning Developer Guide .
Possible values:

REGRESSION
BINARY
MULTICLASS
    # training-data-source-id : The DataSource that points to the training data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("machinelearning", "create-ml-model", "ml-model-id", "ml-model-type", "training-data-source-id", add_option_dict)
