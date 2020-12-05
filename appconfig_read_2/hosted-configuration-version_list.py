#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-hosted-configuration-versions.html
if __name__ == '__main__':
    """
	create-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-hosted-configuration-version.html
	delete-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-hosted-configuration-version.html
	get-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-hosted-configuration-version.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # configuration-profile-id : The configuration profile ID.
    """

    execute_two_parameter("appconfig", "list-hosted-configuration-versions", "application-id", "configuration-profile-id", parameter_display_string)