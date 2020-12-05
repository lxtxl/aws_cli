#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance.html
if __name__ == '__main__':
    """
	create-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html
	reboot-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html
	start-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-instance.html
	stop-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-instance.html
    """

    parameter_display_string = """
    # db-instance-identifier : The DB instance identifier for the DB instance to be deleted. This parameter isnât case-sensitive.
Constraints:

Must match the name of an existing DB instance.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "delete-db-instance", "db-instance-identifier", add_option_dict)





