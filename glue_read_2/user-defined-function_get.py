#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-function.html
if __name__ == '__main__':
    """
	create-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-user-defined-function.html
	delete-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-user-defined-function.html
	get-user-defined-functions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-user-defined-functions.html
	update-user-defined-function : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-user-defined-function.html
    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the function is located.
    # function-name : The name of the function.
    """

    execute_two_parameter("glue", "get-user-defined-function", "database-name", "function-name", parameter_display_string)