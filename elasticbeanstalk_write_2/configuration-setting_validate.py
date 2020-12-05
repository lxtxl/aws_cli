#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/validate-configuration-settings.html
if __name__ == '__main__':
    """
	describe-configuration-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/describe-configuration-settings.html
    """

    parameter_display_string = """
    # application-name : The name of the application that the configuration template or environment belongs to.
    # option-settings : A list of the options and desired values to evaluate.
(structure)

A specification identifying an individual configuration option along with its current value. For a list of possible namespaces and option values, see Option Values in the AWS Elastic Beanstalk Developer Guide .
ResourceName -> (string)

A unique resource name for the option setting. Use it for a timeâbased scaling configuration option.

Namespace -> (string)

A unique namespace that identifies the optionâs associated AWS resource.

OptionName -> (string)

The name of the configuration option.

Value -> (string)

The current value for the configuration option.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticbeanstalk", "validate-configuration-settings", "application-name", "option-settings", add_option_dict)
