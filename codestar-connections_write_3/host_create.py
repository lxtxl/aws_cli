#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-host.html
if __name__ == '__main__':
    """
	delete-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-host.html
	get-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-host.html
	list-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-hosts.html
	update-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-host.html
    """

    parameter_display_string = """
    # name : The name of the host to be created. The name must be unique in the calling AWS account.
    # provider-type : The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.
Possible values:

Bitbucket
GitHub
GitHubEnterpriseServer
    # provider-endpoint : The endpoint of the infrastructure to be represented by the host after it is created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codestar-connections", "create-host", "name", "provider-type", "provider-endpoint", add_option_dict)
