#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html
if __name__ == '__main__':
    """
	delete-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-secret.html
	describe-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/describe-secret.html
	list-secrets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secrets.html
	restore-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/restore-secret.html
	rotate-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/rotate-secret.html
	update-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret.html
    """

    parameter_display_string = """
    # name : Specifies the friendly name of the new secret.
The secret name must be ASCII letters, digits, or the following characters : /_+=.@-

Note
Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters at the end of the ARN.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("secretsmanager", "create-secret", "name", add_option_dict)





