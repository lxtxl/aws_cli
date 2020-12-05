#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy-version.html
if __name__ == '__main__':
    """
	delete-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy-version.html
	get-policy-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy-version.html
	list-policy-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html
    """

    parameter_display_string = """
    # policy-arn : The Amazon Resource Name (ARN) of the IAM policy to which you want to add a new version.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # policy-document : The JSON policy document that you want to use as the content for this new version of the policy.
You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "create-policy-version", "policy-arn", "policy-document", add_option_dict)
