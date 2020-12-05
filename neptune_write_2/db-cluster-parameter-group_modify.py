#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-cluster-parameter-group.html
if __name__ == '__main__':
    """
	copy-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/copy-db-cluster-parameter-group.html
	create-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-cluster-parameter-group.html
	delete-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-cluster-parameter-group.html
	describe-db-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-cluster-parameter-groups.html
	reset-db-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reset-db-cluster-parameter-group.html
    """

    parameter_display_string = """
    # db-cluster-parameter-group-name : The name of the DB cluster parameter group to modify.
    # parameters : A list of parameters in the DB cluster parameter group to modify.
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
    write_two_parameter("neptune", "modify-db-cluster-parameter-group", "db-cluster-parameter-group-name", "parameters", add_option_dict)
