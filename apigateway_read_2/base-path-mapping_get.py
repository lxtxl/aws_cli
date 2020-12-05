#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mapping.html
if __name__ == '__main__':
    """
	create-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-base-path-mapping.html
	delete-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-base-path-mapping.html
	get-base-path-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mappings.html
	update-base-path-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-base-path-mapping.html
    """

    parameter_display_string = """
    # domain-name : [Required] The domain name of the  BasePathMapping resource to be described.
    # base-path : [Required] The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify â(none)â if you do not want callers to specify any base path name after the domain name.
    """

    execute_two_parameter("apigateway", "get-base-path-mapping", "domain-name", "base-path", parameter_display_string)