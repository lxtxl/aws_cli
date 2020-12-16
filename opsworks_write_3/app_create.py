#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-app.html
if __name__ == '__main__':
    """
	delete-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-app.html
	describe-apps : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-apps.html
	update-app : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-app.html
    """

    parameter_display_string = """
    # stack-id : The stack ID.
    # name : The app name.
    # type : The app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isnât one of the standard types, or you prefer to implement your own Deploy recipes, specify other .
Possible values:

aws-flow-ruby
java
rails
php
nodejs
static
other
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("opsworks", "create-app", "stack-id", "name", "type", add_option_dict)
