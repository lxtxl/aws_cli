#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployment.html
if __name__ == '__main__':
    """
	create-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html
	delete-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-deployment.html
	get-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployments.html
	update-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-deployment.html
    """

    parameter_display_string = """
    # rest-api-id : [Required] The string identifier of the associated  RestApi .
    # deployment-id : [Required] The identifier of the  Deployment resource to get information about.
    """

    execute_two_parameter("apigateway", "get-deployment", "rest-api-id", "deployment-id", parameter_display_string)