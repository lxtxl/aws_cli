#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/tag-resource.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-resource.html
	get-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resource.html
	get-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-resource.html
    """

    parameter_display_string = """
    # resource-arn : [Required] The ARN of a resource that can be tagged.
    # tags : [Required] The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws: . The tag value can be up to 256 characters.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("apigateway", "tag-resource", "resource-arn", "tags", add_option_dict)
