#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-domain-association.html
if __name__ == '__main__':
    """
	create-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-domain-association.html
	delete-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-domain-association.html
	get-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-domain-association.html
	list-domain-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-domain-associations.html
    """

    parameter_display_string = """
    # app-id : The unique ID for an Amplify app.
    # domain-name : The name of the domain.
    # sub-domain-settings : Describes the settings for the subdomain.
(structure)

Describes the settings for the subdomain.
prefix -> (string)

The prefix setting for the subdomain.

branchName -> (string)

The branch name setting for the subdomain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("amplify", "update-domain-association", "app-id", "domain-name", "sub-domain-settings", add_option_dict)
