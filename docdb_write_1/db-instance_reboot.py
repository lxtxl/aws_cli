#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reboot-db-instance.html
if __name__ == '__main__':
    """
	create-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-instance.html
	delete-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-instance.html
    """

    parameter_display_string = """
    # db-instance-identifier : The instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must match the identifier of an existing DBInstance .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("docdb", "reboot-db-instance", "db-instance-identifier", add_option_dict)





