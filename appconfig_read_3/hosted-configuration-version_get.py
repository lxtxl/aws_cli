#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-hosted-configuration-version.html
if __name__ == '__main__':
    """
	create-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-hosted-configuration-version.html
	delete-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-hosted-configuration-version.html
	list-hosted-configuration-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-hosted-configuration-versions.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # configuration-profile-id : The configuration profile ID.
    """

    execute_two_parameter("appconfig", "get-hosted-configuration-version", "application-id", "configuration-profile-id", parameter_display_string)