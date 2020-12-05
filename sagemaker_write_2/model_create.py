#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-models.html
    """

    parameter_display_string = """
    # model-name : The name of the new model.
    # execution-role-arn : The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see Amazon SageMaker Roles .

Note
To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-model", "model-name", "execution-role-arn", add_option_dict)
