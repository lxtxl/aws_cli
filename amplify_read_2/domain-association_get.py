#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-domain-association.html
if __name__ == '__main__':
    """
	create-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-domain-association.html
	delete-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-domain-association.html
	list-domain-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-domain-associations.html
	update-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/update-domain-association.html
    """

    parameter_display_string = """
    # app-id : The unique id for an Amplify app.
    # domain-name : The name of the domain.
    """

    execute_two_parameter("amplify", "get-domain-association", "app-id", "domain-name", parameter_display_string)