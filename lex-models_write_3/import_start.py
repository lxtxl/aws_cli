#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/start-import.html
if __name__ == '__main__':
    """
	get-import : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-import.html
    """

    parameter_display_string = """
    # payload : 
    # resource-type : Specifies the type of resource to export. Each resource also exports any resources that it depends on.

A bot exports dependent intents.
An intent exports dependent slot types.

Possible values:

BOT
INTENT
SLOT_TYPE
    # merge-strategy : Specifies the action that the StartImport operation should take when there is an existing resource with the same name.

FAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the failureReason field of the response to the GetImport operation. OVERWRITE_LATEST - The import operation proceeds even if there is a conflict with an existing resource. The $LASTEST version of the existing resource is overwritten with the data from the import file.

Possible values:

OVERWRITE_LATEST
FAIL_ON_CONFLICT
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lex-models", "start-import", "payload", "resource-type", "merge-strategy", add_option_dict)
