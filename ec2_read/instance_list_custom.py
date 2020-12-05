#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	bundle-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/bundle-instance.html
	monitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/monitor-instances.html
	reboot-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reboot-instances.html
	run-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html
	start-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-instances.html
	stop-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html
	terminate-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html
	unmonitor-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unmonitor-instances.html
    """

    parameter_num = len(sys.argv)

    if parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config> <template>".format(sys.argv[0]))
        sys.exit(1)

    profile_name = sys.argv[1]
    template_name = sys.argv[2]

    if template_name == "base":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    InstanceId
                    ,ImageId
                    ,InstanceType
                    ,KeyName
                    ,Monitoring.State
                    ,Placement.AvailabilityZone
                    ,PrivateIpAddress
                    ,PublicIpAddress
                    ,VpcId
                    ,SubnetId
                    ,SecurityGroups[].GroupName|join(',',@)
                    ,BlockDeviceMappings[].DeviceName|join(',',@)
                    ,State.Name
                    ,EbsOptimized,
                    Tags[?Key=='Name'].Value|[0]
                ]
            \"
        """
    elif template_name == "simple":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,PrivateIpAddress
                    ,SecurityGroups[].GroupId|join(',',@)
                    ,InstanceId
                    ,InstanceType
                    ,KeyName
                ]
            \"
        """
    elif template_name == "status":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,State.Name                ]
            \"
        """
    elif template_name == "type":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,InstanceType                ]
            \"
        """
    elif template_name == "ip":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,PublicIpAddress
                    ,PrivateIpAddress
                ]
            \"
        """
    elif template_name == "uid":
        output_name = "text"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    InstanceId
                ]
            \"
        """
    elif template_name == "sg_id":
        output_name = "text"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,SecurityGroups[].GroupId|join(',',@)
                ]
            \"
        """
    elif template_name == "sg_name":
        output_name = "text"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,SecurityGroups[].GroupName|join(',',@)
                ]
            \"
        """
    elif template_name == "input":
        output_name = "table"
        query_name = """\"
            Reservations[*]
                .Instances[*].[
                    Tags[?Key=='Name'].Value|[0]
                    ,InstanceId
                    ,ImageId                                        
                    ,InstanceType
                    ,KeyName
                    ,SecurityGroups[].GroupName|join(',',@)
                    ,VpcId
                    ,SubnetId
                    ,PrivateIpAddress
                    ,PublicIpAddress
                ]
            \"
        """

    change_query_name = query_name.replace("\n", "")
    change_query_name = change_query_name.replace(" ", "")

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # custom parameter
    add_option_dict["output"] = output_name
    add_option_dict["query"] = change_query_name

    read_no_parameter(profile_name, "ec2", "describe-instances", add_option_dict)
