#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/rotate-encryption-key.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier of the cluster that you want to rotate the encryption keys for.
Constraints: Must be the name of valid cluster that has encryption enabled.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "rotate-encryption-key", "cluster-identifier", add_option_dict)





