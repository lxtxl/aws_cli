#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/untag-resource.html
    """

    parameter_display_string = """
    # secret-id : The identifier for the secret that you want to attach tags to. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.

Note
If you specify an ARN, we generally recommend that you specify a complete ARN. You can specify a partial ARN tooâfor example, if you donât include the final hyphen and six random characters that Secrets Manager adds at the end of the ARN when you created the secret. A partial ARN match can work as long as it uniquely matches only one secret. However, if your secret has a name that ends in a hyphen followed by six characters (before Secrets Manager adds the hyphen and six characters to the ARN) and you try to use that as a partial ARN, then those characters cause Secrets Manager to assume that youâre specifying a complete ARN. This confusion can cause unexpected results. To avoid this situation, we recommend that you donât create secret names ending with a hyphen followed by six characters.
If you specify an incomplete ARN without the random suffix, and instead provide the âfriendly nameâ, you must not include the random suffix. If you do include the random suffix added by Secrets Manager, you receive either a ResourceNotFoundException or an AccessDeniedException error, depending on your permissions.
    # tags : The tags to attach to the secret. Each element in the list consists of a Key and a Value .
This parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide . For the AWS CLI, you can also use the syntax: --Tags Key="Key1",Value="Value1",Key="Key2",Value="Value2"[,â¦]
(structure)

A structure that contains information about a tag.
Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value associated with the key of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("secretsmanager", "tag-resource", "secret-id", "tags", add_option_dict)
