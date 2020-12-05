#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/put-policy.html
if __name__ == '__main__':
    """
	delete-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-policy.html
	get-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-policy.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Number (ARN) of the private CA to associate with the policy. The ARN of the CA can be found by calling the ListCertificateAuthorities action.
    # policy : The path and filename of a JSON-formatted IAM policy to attach to the specified private CA resource. If this policy does not contain all required statements or if it includes any statement that is not allowed, the PutPolicy action returns an InvalidPolicyException . For information about IAM policy and statement structure, see Overview of JSON Policies .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("acm-pca", "put-policy", "resource-arn", "policy", add_option_dict)
