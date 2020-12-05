#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-instance.html
if __name__ == '__main__':
    """
	create-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html
	delete-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-instance.html
	describe-replication-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-instances.html
	reboot-replication-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reboot-replication-instance.html
    """

    parameter_display_string = """
    # replication-instance-arn : The Amazon Resource Name (ARN) of the replication instance.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "modify-replication-instance", "replication-instance-arn", add_option_dict)





