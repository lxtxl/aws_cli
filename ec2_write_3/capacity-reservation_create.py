#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html
if __name__ == '__main__':
    """
	cancel-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html
	describe-capacity-reservations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html
	modify-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-capacity-reservation.html
    """

    parameter_display_string = """
    # instance-type : The instance type for which to reserve capacity. For more information, see Instance Types in the Amazon Elastic Compute Cloud User Guide .
    # instance-platform : The type of operating system for which to reserve capacity.
Possible values:

Linux/UNIX
Red Hat Enterprise Linux
SUSE Linux
Windows
Windows with SQL Server
Windows with SQL Server Enterprise
Windows with SQL Server Standard
Windows with SQL Server Web
Linux with SQL Server Standard
Linux with SQL Server Web
Linux with SQL Server Enterprise
    # instance-count : The number of instances for which to reserve capacity.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-capacity-reservation", "instance-type", "instance-platform", "instance-count", add_option_dict)
