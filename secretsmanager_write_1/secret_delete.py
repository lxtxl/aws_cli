#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-secret.html
if __name__ == '__main__':
    """
	create-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html
	describe-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/describe-secret.html
	list-secrets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secrets.html
	restore-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/restore-secret.html
	rotate-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/rotate-secret.html
	update-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret.html
    """

    parameter_display_string = """
    # secret-id : Specifies the secret that you want to delete. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.

Note
If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN tooâfor example, if you donât include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that youâre specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you donât create secret names ending with a hyphen followed by six characters.
If you specify an incomplete ARN without the random suffix, and instead provide the âfriendly nameâ, you must not include the random suffix. If you do include the random suffix added by Secrets Manager, you receive either a ResourceNotFoundException or an AccessDeniedException error, depending on your permissions.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("secretsmanager", "delete-secret", "secret-id", add_option_dict)





