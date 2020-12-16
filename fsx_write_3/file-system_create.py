#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-system.html
if __name__ == '__main__':
    """
	delete-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-file-system.html
	describe-file-systems : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-systems.html
	update-file-system : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-file-system.html
    """

    parameter_display_string = """
    # file-system-type : The type of Amazon FSx file system to create, either WINDOWS or LUSTRE .
Possible values:

WINDOWS
LUSTRE
    # storage-capacity : Sets the storage capacity of the file system that youâre creating.
For Lustre file systems:

For SCRATCH_2 and PERSISTENT_1 SSD deployment types, valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.
For PERSISTENT HDD file systems, valid values are increments of 6000 GiB for 12 MB/s/TiB file systems and increments of 1800 GiB for 40 MB/s/TiB file systems.
For SCRATCH_1 deployment type, valid values are 1200 GiB, 2400 GiB, and increments of 3600 GiB.

For Windows file systems:

If StorageType=SSD , valid values are 32 GiB - 65,536 GiB (64 TiB).
If StorageType=HDD , valid values are 2000 GiB - 65,536 GiB (64 TiB).
    # subnet-ids : Specifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.
For Windows SINGLE_AZ_1 and SINGLE_AZ_2 file system deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnetâs Availability Zone.
(string)

The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("fsx", "create-file-system", "file-system-type", "storage-capacity", "subnet-ids", add_option_dict)
