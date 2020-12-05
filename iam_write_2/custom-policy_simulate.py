#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/simulate-custom-policy.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # policy-input-list : A list of policy documents to include in the simulation. Each document is specified as a string containing the complete, valid JSON text of an IAM policy. Do not include any resource-based policies in this parameter. Any resource-based policy must be submitted with the ResourcePolicy parameter. The policies cannot be âscope-downâ policies, such as you could include in a call to GetFederationToken or one of the AssumeRole API operations. In other words, do not use policies designed to restrict what a user can do while using the temporary credentials.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )

(string)
    # action-names : A list of names of API operations to evaluate in the simulation. Each operation is evaluated against each resource. Each operation must include the service identifier, such as iam:CreateUser . This operation does not support using wildcards (*) in an action name.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "simulate-custom-policy", "policy-input-list", "action-names", add_option_dict)
