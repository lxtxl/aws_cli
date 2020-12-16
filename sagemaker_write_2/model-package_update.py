#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-model-package.html
if __name__ == '__main__':
    """
	create-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html
	delete-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model-package.html
	describe-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-model-package.html
	list-model-packages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-model-packages.html
    """

    parameter_display_string = """
    # model-package-arn : The Amazon Resource Name (ARN) of the model.
    # model-approval-status : The approval status of the model.
Possible values:

Approved
Rejected
PendingManualApproval
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "update-model-package", "model-package-arn", "model-approval-status", add_option_dict)
