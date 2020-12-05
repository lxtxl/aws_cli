#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html
if __name__ == '__main__':
    """
	create-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html
	delete-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html
	describe-cluster-parameter-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html
	reset-cluster-parameter-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html
    """

    parameter_display_string = """
    # parameter-group-name : The name of the parameter group to be modified.
    # parameters : An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.
For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
(structure)

Describes a parameter in a cluster parameter group.
ParameterName -> (string)

The name of the parameter.

ParameterValue -> (string)

The value of the parameter.

Description -> (string)

A description of the parameter.

Source -> (string)

The source of the parameter value, such as âengine-defaultâ or âuserâ.

DataType -> (string)

The data type of the parameter.

AllowedValues -> (string)

The valid range of values for the parameter.

ApplyType -> (string)

Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to Amazon Redshift Parameter Groups in the Amazon Redshift Cluster Management Guide .

IsModifiable -> (boolean)

If true , the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

MinimumEngineVersion -> (string)

The earliest engine version to which the parameter can apply.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "modify-cluster-parameter-group", "parameter-group-name", "parameters", add_option_dict)
