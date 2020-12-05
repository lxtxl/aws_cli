#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html
if __name__ == '__main__':
    """
	delete-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-fleets.html
	describe-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleets.html
	modify-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-fleet.html
    """

    parameter_display_string = """
    # launch-template-configs : The configuration for the EC2 Fleet.
(structure)

Describes a launch template and overrides.
LaunchTemplateSpecification -> (structure)

The launch template to use. You must specify either the launch template ID or launch template name in the request.
LaunchTemplateId -> (string)

The ID of the launch template. If you specify the template ID, you canât specify the template name.

LaunchTemplateName -> (string)

The name of the launch template. If you specify the template name, you canât specify the template ID.

Version -> (string)

The launch template version number, $Latest , or $Default . You must specify a value, otherwise the request fails.
If the value is $Latest , Amazon EC2 uses the latest version of the launch template.
If the value is $Default , Amazon EC2 uses the default version of the launch template.


Overrides -> (list)

Any parameters that you specify override the same parameters in the launch template.
(structure)

Describes overrides for a launch template.
InstanceType -> (string)

The instance type.

MaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance.

SubnetId -> (string)

The IDs of the subnets in which to launch the instances. Separate multiple subnet IDs using commas (for example, subnet-1234abcdeexample1, subnet-0987cdef6example2 ). A request of type instant can have only one subnet ID.

AvailabilityZone -> (string)

The Availability Zone in which to launch the instances.

WeightedCapacity -> (double)

The number of units provided by the specified instance type.

Priority -> (double)

The priority for the launch template override. If AllocationStrategy is set to prioritized , EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. Valid values are whole numbers starting at 0 . The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority.

Placement -> (structure)

The location where the instance launched, if applicable.
AvailabilityZone -> (string)

The Availability Zone of the instance.
If not specified, an Availability Zone will be automatically chosen for you based on the load balancing criteria for the Region.
This parameter is not supported by CreateFleet .

Affinity -> (string)

The affinity setting for the instance on the Dedicated Host. This parameter is not supported for the ImportInstance command.
This parameter is not supported by CreateFleet .

GroupName -> (string)

The name of the placement group the instance is in.

PartitionNumber -> (integer)

The number of the partition the instance is in. Valid only if the placement group strategy is set to partition .
This parameter is not supported by CreateFleet .

HostId -> (string)

The ID of the Dedicated Host on which the instance resides. This parameter is not supported for the ImportInstance command.
This parameter is not supported by CreateFleet .

Tenancy -> (string)

The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. The host tenancy is not supported for the ImportInstance command.
This parameter is not supported by CreateFleet .

SpreadDomain -> (string)

Reserved for future use.
This parameter is not supported by CreateFleet .

HostResourceGroupArn -> (string)

The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the Tenancy parameter or set it to host .
This parameter is not supported by CreateFleet .
    # target-capacity-specification : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-fleet", "launch-template-configs", "target-capacity-specification", add_option_dict)
