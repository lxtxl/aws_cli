#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html
if __name__ == '__main__':
    """
	delete-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html
	list-service-specific-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html
	reset-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html
	update-service-specific-credential : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html
    """

    parameter_display_string = """
    # user-name : The name of the IAM user that is to be associated with the credentials. The new service-specific credentials have the same permissions as the associated user except that they can be used only to access the specified service.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # service-name : The name of the AWS service that is to be associated with the credentials. The service you specify here is the only service that can be accessed using these credentials.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "create-service-specific-credential", "user-name", "service-name", add_option_dict)
