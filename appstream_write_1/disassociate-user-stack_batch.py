#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/batch-disassociate-user-stack.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-stack-associations : The list of UserStackAssociation objects.
(structure)

Describes a user in the user pool and the associated stack.
StackName -> (string)

The name of the stack that is associated with the user.

UserName -> (string)

The email address of the user who is associated with the stack.

Note
Usersâ email addresses are case-sensitive.


AuthenticationType -> (string)

The authentication type for the user.

SendEmailNotification -> (boolean)

Specifies whether a welcome email is sent to a user after the user is created in the user pool.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("appstream", "batch-disassociate-user-stack", "user-stack-associations", add_option_dict)





