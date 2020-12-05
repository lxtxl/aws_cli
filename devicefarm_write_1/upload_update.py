#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-upload.html
if __name__ == '__main__':
    """
	create-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html
	delete-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-upload.html
	get-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html
	list-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-uploads.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the uploaded test spec.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "update-upload", "arn", add_option_dict)





