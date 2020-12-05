#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html
if __name__ == '__main__':
    """
	delete-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-deployment.html
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployment.html
	get-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployments.html
	update-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-deployment.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "create-deployment", "rest-api-id", add_option_dict)





