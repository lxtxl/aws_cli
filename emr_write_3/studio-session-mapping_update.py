#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/update-studio-session-mapping.html
if __name__ == '__main__':
    """
	create-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio-session-mapping.html
	delete-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-studio-session-mapping.html
	get-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-studio-session-mapping.html
	list-studio-session-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-studio-session-mappings.html
    """

    parameter_display_string = """
    # studio-id : The ID of the EMR Studio.
    # identity-type : Specifies whether the identity to update is a user or a group.
Possible values:

USER
GROUP
    # session-policy-arn : The Amazon Resource Name (ARN) of the session policy to associate with the specified user or group.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("emr", "update-studio-session-mapping", "studio-id", "identity-type", "session-policy-arn", add_option_dict)
