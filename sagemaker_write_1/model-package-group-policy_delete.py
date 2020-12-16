#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model-package-group-policy.html
if __name__ == '__main__':
    """
	get-model-package-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/get-model-package-group-policy.html
	put-model-package-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/put-model-package-group-policy.html
    """

    parameter_display_string = """
    # model-package-group-name : The name of the model group for which to delete the policy.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-model-package-group-policy", "model-package-group-name", add_option_dict)





