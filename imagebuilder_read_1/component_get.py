#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html
if __name__ == '__main__':
    """
	create-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-component.html
	delete-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-component.html
	import-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-component.html
	list-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-components.html
    """

    parameter_display_string = """
    # component-build-version-arn : The Amazon Resource Name (ARN) of the component that you want to retrieve. Regex requires â/d+$â suffix.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("imagebuilder", "get-component", "component-build-version-arn", add_option_dict)