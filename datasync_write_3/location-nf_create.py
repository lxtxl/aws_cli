#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-nfs.html
if __name__ == '__main__':
    """
	describe-location-nfs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-location-nfs.html
    """

    parameter_display_string = """
    # subdirectory : The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination. The NFS path should be a path thatâs exported by the NFS server, or a subdirectory of that path. The path should be such that it can be mounted by other NFS clients in your network.
To see all the paths exported by your NFS server, run âshowmount -e nfs-server-name â from an NFS client that has access to your server. You can specify any directory that appears in the results, and any subdirectory of that directory. Ensure that the NFS export is accessible without Kerberos authentication.
To transfer all the data in the folder you specified, DataSync needs to have permissions to read all the data. To ensure this, either configure the NFS export with no_root_squash, or ensure that the permissions for all of the files that you want DataSync allow read access for all users. Doing either enables the agent to read the files. For the agent to access directories, you must additionally enable all execute access.
If you are copying data to or from your AWS Snowcone device, see NFS Server on AWS Snowcone for more information.
For information about NFS export configuration, see 18.7. The /etc/exports Configuration File in the Red Hat Enterprise Linux documentation.
    # server-hostname : The name of the NFS server. This value is the IP address or Domain Name Service (DNS) name of the NFS server. An agent that is installed on-premises uses this host name to mount the NFS server in a network.
If you are copying data to or from your AWS Snowcone device, see NFS Server on AWS Snowcone for more information.

Note
This name must either be DNS-compliant or must be an IP version 4 (IPv4) address.
    # on-prem-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("datasync", "create-location-nfs", "subdirectory", "server-hostname", "on-prem-config", add_option_dict)
