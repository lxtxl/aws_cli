#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-parameter-group.html
	create-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-parameter-group.html
	delete-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-parameter-group.html
	describe-db-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-parameter-groups.html
	reset-db-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reset-db-parameter-group.html
    """

    parameter_display_string = """
    # db-parameter-group-name : The name of the DB parameter group.
Constraints:

If supplied, must match the name of an existing DBParameterGroup.
    # parameters : An array of parameter names, values, and the apply method for the parameter update. At least one parameter name, value, and apply method must be supplied; subsequent arguments are optional. A maximum of 20 parameters can be modified in a single request.
Valid Values (for the application method): immediate | pending-reboot

Note
You can use the immediate value with dynamic parameters only. You can use the pending-reboot value for both dynamic and static parameters, and changes are applied when you reboot the DB instance without failover.

(structure)

Specifies a parameter.
ParameterName -> (string)

Specifies the name of the parameter.

ParameterValue -> (string)

Specifies the value of the parameter.

Description -> (string)

Provides a description of the parameter.

Source -> (string)

Indicates the source of the parameter value.

ApplyType -> (string)

Specifies the engine specific parameters type.

DataType -> (string)

Specifies the valid data type for the parameter.

AllowedValues -> (string)

Specifies the valid range of values for the parameter.

IsModifiable -> (boolean)

Indicates whether (true ) or not (false ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion -> (string)

The earliest engine version to which the parameter can apply.

ApplyMethod -> (string)

Indicates when to apply parameter updates.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("neptune", "modify-db-parameter-group", "db-parameter-group-name", "parameters", add_option_dict)
