#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-client-certificate.html
if __name__ == '__main__':
    """
	delete-hsm-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-client-certificate.html
	describe-hsm-client-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-client-certificates.html
    """

    parameter_display_string = """
    # hsm-client-certificate-identifier : The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "create-hsm-client-certificate", "hsm-client-certificate-identifier", add_option_dict)





