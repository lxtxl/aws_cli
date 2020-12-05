#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows-for-target.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # targets : The instance ID or key/value pair to retrieve information about.
(structure)

An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
Run Command and Maintenance window targets only : ``Key=resource-groups:Name,Values=*resource-group-name* ``
Maintenance window targets only : ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
Automation targets only : ``Key=ResourceGroup;Values=*resource-group-name* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
Run Command and Maintenance window targets only : Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
Maintenance window targets only : ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
Automation targets only : Key=ResourceGroup,Values=MyResourceGroup
State Manager association targets only : Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For more information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .
Key -> (string)

User-defined criteria for sending commands that target instances that meet the criteria.

Values -> (list)

User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .
(string)
    # resource-type : The type of resource you want to retrieve information about. For example, âINSTANCEâ.
Possible values:

INSTANCE
RESOURCE_GROUP
    """

    execute_two_parameter("ssm", "describe-maintenance-windows-for-target", "targets", "resource-type", parameter_display_string)