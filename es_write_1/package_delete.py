#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-package.html
if __name__ == '__main__':
    """
	associate-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/associate-package.html
	create-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-package.html
	describe-packages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-packages.html
	dissociate-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/dissociate-package.html
	update-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-package.html
    """

    parameter_display_string = """
    # package-id : Internal ID of the package that you want to delete. Use DescribePackages to find this value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("es", "delete-package", "package-id", add_option_dict)





