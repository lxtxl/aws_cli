#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model-package.html
if __name__ == '__main__':
    """
	create-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html
	describe-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-model-package.html
	list-model-packages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-model-packages.html
    """

    parameter_display_string = """
    # model-package-name : The name of the model package. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-model-package", "model-package-name", add_option_dict)





