#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-relational-database-parameters.html
if __name__ == '__main__':
    """
	get-relational-database-parameters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-parameters.html
    """

    parameter_display_string = """
    # relational-database-name : The name of your database for which to update parameters.
    # parameters : The database parameters to update.
(structure)

Describes the parameters of a database.
allowedValues -> (string)

Specifies the valid range of values for the parameter.

applyMethod -> (string)

Indicates when parameter updates are applied.
Can be immediate or pending-reboot .

applyType -> (string)

Specifies the engine-specific parameter type.

dataType -> (string)

Specifies the valid data type for the parameter.

description -> (string)

Provides a description of the parameter.

isModifiable -> (boolean)

A Boolean value indicating whether the parameter can be modified.

parameterName -> (string)

Specifies the name of the parameter.

parameterValue -> (string)

Specifies the value of the parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "update-relational-database-parameters", "relational-database-name", "parameters", add_option_dict)
