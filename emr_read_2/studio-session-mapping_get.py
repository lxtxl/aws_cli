#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-studio-session-mapping.html
if __name__ == '__main__':
    """
	create-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio-session-mapping.html
	delete-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-studio-session-mapping.html
	list-studio-session-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-studio-session-mappings.html
	update-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/update-studio-session-mapping.html
    """

    parameter_display_string = """
    # studio-id : The ID of the Amazon EMR Studio.
    # identity-type : Specifies whether the identity to fetch is a user or a group.
Possible values:

USER
GROUP
    """

    execute_two_parameter("emr", "get-studio-session-mapping", "studio-id", "identity-type", parameter_display_string)