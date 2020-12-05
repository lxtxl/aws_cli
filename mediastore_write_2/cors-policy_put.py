#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html
if __name__ == '__main__':
    """
	delete-cors-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-cors-policy.html
	get-cors-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html
    """

    parameter_display_string = """
    # container-name : The name of the container that you want to assign the CORS policy to.
    # cors-policy : The CORS policy to apply to the container.
(structure)

A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.
AllowedOrigins -> (list)

One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
Each CORS rule must have at least one AllowedOrigins element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.
(string)

AllowedMethods -> (list)

Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.
Each CORS rule must contain at least one AllowedMethods and one AllowedOrigins element.
(string)

AllowedHeaders -> (list)

Specifies which headers are allowed in a preflight OPTIONS request through the Access-Control-Request-Headers header. Each header name that is specified in Access-Control-Request-Headers must have a corresponding entry in the rule. Only the headers that were requested are sent back.
This element can contain only one wildcard character (*).
(string)

MaxAgeSeconds -> (integer)

The time in seconds that your browser caches the preflight response for the specified resource.
A CORS rule can have only one MaxAgeSeconds element.

ExposeHeaders -> (list)

One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).
This element is optional for each rule.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediastore", "put-cors-policy", "container-name", "cors-policy", add_option_dict)
