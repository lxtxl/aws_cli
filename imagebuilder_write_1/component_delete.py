#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-component.html
if __name__ == '__main__':
    """
	create-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-component.html
	get-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html
	import-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-component.html
	list-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-components.html
    """

    parameter_display_string = """
    # component-build-version-arn : The Amazon Resource Name (ARN) of the component build version to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "delete-component", "component-build-version-arn", add_option_dict)





