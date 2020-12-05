#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-task-definition.html
if __name__ == '__main__':
    """
	deregister-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deregister-task-definition.html
	describe-task-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-task-definition.html
	list-task-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-task-definitions.html
    """

    parameter_display_string = """
    # family : You must specify a family for a task definition, which allows you to track multiple versions of the same task definition. The family is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, and hyphens are allowed.
    # container-definitions : A list of container definitions in JSON format that describe the different containers that make up your task.
(structure)

Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
name -> (string)

The name of a container. If you are linking multiple containers together in a task definition, the name of one container can be entered in the links of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, and hyphens are allowed. This parameter maps to name in the Create a container section of the Docker Remote API and the --name option to docker run .

image -> (string)

The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` repository-url /image :tag `` or `` repository-url /image @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run .

When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.
Images in Amazon ECR repositories can be specified by either using the full registry/repository:tag or registry/repository@digest . For example, 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest or 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE .
Images in official repositories on Docker Hub use a single name (for example, ubuntu or mongo ).
Images in other repositories on Docker Hub are qualified with an organization name (for example, amazon/amazon-ecs-agent ).
Images in other online repositories are qualified further by a domain name (for example, quay.io/assemblyline/ubuntu ).


repositoryCredentials -> (structure)

The private repository authentication credentials to use.
credentialsParameter -> (string)

The Amazon Resource Name (ARN) of the secret containing the private repository credentials.

Note
When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.



cpu -> (integer)

The number of cpu units reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run .
This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level cpu value.

Note
You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the Amazon EC2 Instances detail page by 1,024.

Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see CPU share constraint in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:

Agent versions less than or equal to 1.1.0: Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares.
Agent versions greater than or equal to 1.2.0: Null, zero, and CPU values of 1 are passed to Docker as 2.

On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition. A null or zero CPU value is passed to Docker as 0 , which Windows interprets as 1% of one CPU.

memory -> (integer)

The amount (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. The total amount of memory reserved for all containers within a task must be lower than the task memory value, if one is specified. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run .
If using the Fargate launch type, this parameter is optional.
If using the EC2 launch type, you must specify either a task-level memory value or a container-level memory value. If you specify both a container-level memory and memoryReservation value, memory must be greater than memoryReservation . If you specify memoryReservation , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of memory is used.
The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.

memoryReservation -> (integer)

The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the memory parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to MemoryReservation in the Create a container section of the Docker Remote API and the --memory-reservation option to docker run .
If a task-level memory value is not specified, you must specify a non-zero integer for one or both of memory or memoryReservation in a container definition. If you specify both, memory must be greater than memoryReservation . If you specify memoryReservation , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of memory is used.
For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a memoryReservation of 128 MiB, and a memory hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.

links -> (list)

The links parameter allows containers to communicate with each other without the need for port mappings. This parameter is only supported if the network mode of a task definition is bridge . The name:internalName construct is analogous to name:alias in Docker links. Up to 255 letters (uppercase and lowercase), numbers, and hyphens are allowed. For more information about linking Docker containers, go to Legacy container links in the Docker documentation. This parameter maps to Links in the Create a container section of the Docker Remote API and the --link option to docker run .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.


Warning
Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.

(string)

portMappings -> (list)

The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
For task definitions that use the awsvpc network mode, you should only specify the containerPort . The hostPort can be left blank or it must be the same value as the containerPort .
Port mappings on Windows use the NetNAT gateway address rather than localhost . There is no loopback for port mappings on Windows, so you cannot access a containerâs mapped port from the host itself.
This parameter maps to PortBindings in the Create a container section of the Docker Remote API and the --publish option to docker run . If the network mode of a task definition is set to none , then you canât specify port mappings. If the network mode of a task definition is set to host , then host ports must either be undefined or they must match the container port in the port mapping.

Note
After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the Network Bindings section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the networkBindings section  DescribeTasks responses.

(structure)

Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
If you are using containers in a task with the awsvpc or host network mode, exposed ports should be specified using containerPort . The hostPort can be left blank or it must be the same value as the containerPort .
After a task reaches the RUNNING status, manual and automatic host and container port assignments are visible in the networkBindings section of  DescribeTasks API responses.
containerPort -> (integer)

The port number on the container that is bound to the user-specified or automatically assigned host port.
If you are using containers in a task with the awsvpc or host network mode, exposed ports should be specified using containerPort .
If you are using containers in a task with the bridge network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see hostPort . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.

hostPort -> (integer)

The port number on the container instance to reserve for your container.
If you are using containers in a task with the awsvpc or host network mode, the hostPort can either be left blank or set to the same value as the containerPort .
If you are using containers in a task with the bridge network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the hostPort (or set it to 0 ) while specifying a containerPort and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under /proc/sys/net/ipv4/ip_local_port_range . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.

Note
The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.

The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the remainingResources of  DescribeContainerInstances output. A container instance can have up to 100 reserved ports at a time, including the default reserved ports. Automatically assigned ports donât count toward the 100 reserved ports limit.

protocol -> (string)

The protocol used for the port mapping. Valid values are tcp and udp . The default is tcp .



essential -> (boolean)

If the essential parameter of a container is marked as true , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the essential parameter of a container is marked as false , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see Application Architecture in the Amazon Elastic Container Service Developer Guide .

entryPoint -> (list)


Warning
Early versions of the Amazon ECS container agent do not properly handle entryPoint parameters. If you have problems using entryPoint , update your container agent or enter your commands and arguments as command array items instead.

The entry point that is passed to the container. This parameter maps to Entrypoint in the Create a container section of the Docker Remote API and the --entrypoint option to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#entrypoint .
(string)

command -> (list)

The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run . For more information, see https://docs.docker.com/engine/reference/builder/#cmd . If there are multiple arguments, each argument should be a separated string in the array.
(string)

environment -> (list)

The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run .

Warning
We do not recommend using plaintext environment variables for sensitive information, such as credential data.

(structure)

A key-value pair object.
name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.



environmentFiles -> (list)

A list of files containing the environment variables to pass to a container. This parameter maps to the --env-file option to docker run .
You can specify up to ten environment files. The file must have a .env file extension. Each line in an environment file should contain an environment variable in VARIABLE=VALUE format. Lines beginning with # are treated as comments and are ignored. For more information on the environment variable file syntax, see Declare default environment variables in file .
If there are environment variables specified using the environment parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they are processed from the top down. It is recommended to use unique variable names. For more information, see Specifying Environment Variables in the Amazon Elastic Container Service Developer Guide .
This field is not valid for containers in tasks using the Fargate launch type.
(structure)

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a .env file extension. Each line in an environment file should contain an environment variable in VARIABLE=VALUE format. Lines beginning with # are treated as comments and are ignored. For more information on the environment variable file syntax, see Declare default environment variables in file .
If there are environment variables specified using the environment parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they are processed from the top down. It is recommended to use unique variable names. For more information, see Specifying Environment Variables in the Amazon Elastic Container Service Developer Guide .
This field is not valid for containers in tasks using the Fargate launch type.
value -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

type -> (string)

The file type to use. The only supported value is s3 .



mountPoints -> (list)

The mount points for data volumes in your container.
This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run .
Windows containers can mount whole directories on the same drive as $env:ProgramData . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
(structure)

Details on a volume mount point that is used in a container definition.
sourceVolume -> (string)

The name of the volume to mount. Must be a volume name referenced in the name parameter of task definition volume .

containerPath -> (string)

The path on the container to mount the host volume at.

readOnly -> (boolean)

If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume. The default value is false .



volumesFrom -> (list)

Data volumes to mount from another container. This parameter maps to VolumesFrom in the Create a container section of the Docker Remote API and the --volumes-from option to docker run .
(structure)

Details on a data volume from another container in the same task definition.
sourceContainer -> (string)

The name of another container within the same task definition from which to mount volumes.

readOnly -> (boolean)

If this value is true , the container has read-only access to the volume. If this value is false , then the container can write to the volume. The default value is false .



linuxParameters -> (structure)

Linux-specific modifications that are applied to the container, such as Linux kernel capabilities. For more information see  KernelCapabilities .

Note
This parameter is not supported for Windows containers.

capabilities -> (structure)

The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.

Note
For tasks that use the Fargate launch type, capabilities is supported for all platform versions but the add parameter is only supported if using platform version 1.4.0 or later.

add -> (list)

The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to CapAdd in the Create a container section of the Docker Remote API and the --cap-add option to docker run .

Note
Tasks launched on AWS Fargate only support adding the SYS_PTRACE kernel capability.

Valid values: "ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"
(string)

drop -> (list)

The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to CapDrop in the Create a container section of the Docker Remote API and the --cap-drop option to docker run .
Valid values: "ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"
(string)


devices -> (list)

Any host devices to expose to the container. This parameter maps to Devices in the Create a container section of the Docker Remote API and the --device option to docker run .

Note
If you are using tasks that use the Fargate launch type, the devices parameter is not supported.

(structure)

An object representing a container instance host device.
hostPath -> (string)

The path for the device on the host container instance.

containerPath -> (string)

The path inside the container at which to expose the host device.

permissions -> (list)

The explicit permissions to provide to the container for the device. By default, the container has permissions for read , write , and mknod for the device.
(string)



initProcessEnabled -> (boolean)

Run an init process inside the container that forwards signals and reaps processes. This parameter maps to the --init option to docker run . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'

sharedMemorySize -> (integer)

The value for the size (in MiB) of the /dev/shm volume. This parameter maps to the --shm-size option to docker run .

Note
If you are using tasks that use the Fargate launch type, the sharedMemorySize parameter is not supported.


tmpfs -> (list)

The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the --tmpfs option to docker run .

Note
If you are using tasks that use the Fargate launch type, the tmpfs parameter is not supported.

(structure)

The container path, mount options, and size of the tmpfs mount.
containerPath -> (string)

The absolute file path where the tmpfs volume is to be mounted.

size -> (integer)

The maximum size (in MiB) of the tmpfs volume.

mountOptions -> (list)

The list of tmpfs volume mount options.
Valid values: "defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"
(string)



maxSwap -> (integer)

The total amount of swap memory (in MiB) a container can use. This parameter will be translated to the --memory-swap option to docker run where the value would be the sum of the container memory plus the maxSwap value.
If a maxSwap value of 0 is specified, the container will not use swap. Accepted values are 0 or any positive integer. If the maxSwap parameter is omitted, the container will use the swap configuration for the container instance it is running on. A maxSwap value must be set for the swappiness parameter to be used.

Note
If you are using tasks that use the Fargate launch type, the maxSwap parameter is not supported.


swappiness -> (integer)

This allows you to tune a containerâs memory swappiness behavior. A swappiness value of 0 will cause swapping to not happen unless absolutely necessary. A swappiness value of 100 will cause pages to be swapped very aggressively. Accepted values are whole numbers between 0 and 100 . If the swappiness parameter is not specified, a default value of 60 is used. If a value is not specified for maxSwap then this parameter is ignored. This parameter maps to the --memory-swappiness option to docker run .

Note
If you are using tasks that use the Fargate launch type, the swappiness parameter is not supported.



secrets -> (list)

The secrets to pass to the container. For more information, see Specifying Sensitive Data in the Amazon Elastic Container Service Developer Guide .
(structure)

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:

To inject sensitive data into your containers as environment variables, use the secrets container definition parameter.
To reference sensitive information in the log configuration of a container, use the secretOptions container definition parameter.

For more information, see Specifying Sensitive Data in the Amazon Elastic Container Service Developer Guide .
name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.

Note
If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.




dependsOn -> (list)

The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ecs-init package. If your container instances are launched from version 20190301 or later, then they contain the required versions of the container agent and ecs-init . For more information, see Amazon ECS-optimized Linux AMI in the Amazon Elastic Container Service Developer Guide .
For tasks using the Fargate launch type, the task or service requires platform version 1.3.0 or later.
(structure)

The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
Your Amazon ECS container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ecs-init package. If your container instances are launched from version 20190301 or later, then they contain the required versions of the container agent and ecs-init . For more information, see Amazon ECS-optimized Linux AMI in the Amazon Elastic Container Service Developer Guide .

Note
For tasks using the Fargate launch type, this parameter requires that the task or service uses platform version 1.3.0 or later.

containerName -> (string)

The name of a container.

condition -> (string)

The dependency condition of the container. The following are the available conditions and their behavior:

START - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.
COMPLETE - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition cannot be set on an essential container.
SUCCESS - This condition is the same as COMPLETE , but it also requires that the container exits with a zero status. This condition cannot be set on an essential container.
HEALTHY - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup.




startTimeout -> (integer)

Time duration (in seconds) to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a COMPLETE , SUCCESS , or HEALTHY status. If a startTimeout value is specified for containerB and it does not reach the desired status within that time then containerA will give up and not start. This results in the task transitioning to a STOPPED state.

Note
When the ECS_CONTAINER_START_TIMEOUT container agent configuration variable is used, it is enforced indendently from this start timeout value.

For tasks using the Fargate launch type, this parameter requires that the task or service uses platform version 1.3.0 or later.
For tasks using the EC2 launch type, your container instances require at least version 1.26.0 of the container agent to enable a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ecs-init package. If your container instances are launched from version 20190301 or later, then they contain the required versions of the container agent and ecs-init . For more information, see Amazon ECS-optimized Linux AMI in the Amazon Elastic Container Service Developer Guide .

stopTimeout -> (integer)

Time duration (in seconds) to wait before the container is forcefully killed if it doesnât exit normally on its own.
For tasks using the Fargate launch type, the task or service requires platform version 1.3.0 or later. The max stop timeout value is 120 seconds and if the parameter is not specified, the default value of 30 seconds is used.
For tasks using the EC2 launch type, if the stopTimeout parameter is not specified, the value set for the Amazon ECS container agent configuration variable ECS_CONTAINER_STOP_TIMEOUT is used by default. If neither the stopTimeout parameter or the ECS_CONTAINER_STOP_TIMEOUT agent configuration variable are set, then the default values of 30 seconds for Linux containers and 30 seconds on Windows containers are used. Your container instances require at least version 1.26.0 of the container agent to enable a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see Updating the Amazon ECS Container Agent in the Amazon Elastic Container Service Developer Guide . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ecs-init package. If your container instances are launched from version 20190301 or later, then they contain the required versions of the container agent and ecs-init . For more information, see Amazon ECS-optimized Linux AMI in the Amazon Elastic Container Service Developer Guide .

hostname -> (string)

The hostname to use for your container. This parameter maps to Hostname in the Create a container section of the Docker Remote API and the --hostname option to docker run .

Note
The hostname parameter is not supported if you are using the awsvpc network mode.


user -> (string)

The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run .
You can use the following formats. If specifying a UID or GID, you must specify it as a positive integer.

user
user:group
uid
uid:gid
user:gid
uid:group


Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.


workingDirectory -> (string)

The working directory in which to run commands inside the container. This parameter maps to WorkingDir in the Create a container section of the Docker Remote API and the --workdir option to docker run .

disableNetworking -> (boolean)

When this parameter is true, networking is disabled within the container. This parameter maps to NetworkDisabled in the Create a container section of the Docker Remote API .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.


privileged -> (boolean)

When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run .

Note
This parameter is not supported for Windows containers or tasks using the Fargate launch type.


readonlyRootFilesystem -> (boolean)

When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.


dnsServers -> (list)

A list of DNS servers that are presented to the container. This parameter maps to Dns in the Create a container section of the Docker Remote API and the --dns option to docker run .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.

(string)

dnsSearchDomains -> (list)

A list of DNS search domains that are presented to the container. This parameter maps to DnsSearch in the Create a container section of the Docker Remote API and the --dns-search option to docker run .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.

(string)

extraHosts -> (list)

A list of hostnames and IP address mappings to append to the /etc/hosts file on the container. This parameter maps to ExtraHosts in the Create a container section of the Docker Remote API and the --add-host option to docker run .

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.

(structure)

Hostnames and IP address entries that are added to the /etc/hosts file of a container via the extraHosts parameter of its  ContainerDefinition .
hostname -> (string)

The hostname to use in the /etc/hosts entry.

ipAddress -> (string)

The IP address to use in the /etc/hosts entry.



dockerSecurityOptions -> (list)

A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
With Windows containers, this parameter can be used to reference a credential spec file when configuring a container for Active Directory authentication. For more information, see Using gMSAs for Windows Containers in the Amazon Elastic Container Service Developer Guide .
This parameter maps to SecurityOpt in the Create a container section of the Docker Remote API and the --security-opt option to docker run .

Note
The Amazon ECS container agent running on a container instance must register with the ECS_SELINUX_CAPABLE=true or ECS_APPARMOR_CAPABLE=true environment variables before containers placed on that instance can use these security options. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide .

For more information about valid values, see Docker Run Security Configuration .
Valid values: âno-new-privilegesâ | âapparmor:PROFILEâ | âlabel:valueâ | âcredentialspec:CredentialSpecFilePathâ
(string)

interactive -> (boolean)

When this parameter is true , this allows you to deploy containerized applications that require stdin or a tty to be allocated. This parameter maps to OpenStdin in the Create a container section of the Docker Remote API and the --interactive option to docker run .

pseudoTerminal -> (boolean)

When this parameter is true , a TTY is allocated. This parameter maps to Tty in the Create a container section of the Docker Remote API and the --tty option to docker run .

dockerLabels -> (map)

A key/value map of labels to add to the container. This parameter maps to Labels in the Create a container section of the Docker Remote API and the --label option to docker run . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
key -> (string)
value -> (string)

ulimits -> (list)

A list of ulimits to set in the container. If a ulimit value is specified in a task definition, it will override the default values set by Docker. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'

Note
This parameter is not supported for Windows containers or tasks that use the awsvpc network mode.

(structure)

The ulimit settings to pass to the container.
name -> (string)

The type of the ulimit .

softLimit -> (integer)

The soft limit for the ulimit type.

hardLimit -> (integer)

The hard limit for the ulimit type.



logConfiguration -> (structure)

The log configuration specification for the container.
This parameter maps to LogConfig in the Create a container section of the Docker Remote API and the --log-driver option to docker run . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see Configure logging drivers in the Docker documentation.

Note
Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.

This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'

Note
The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ECS_AVAILABLE_LOGGING_DRIVERS environment variable before containers placed on that instance can use these log configuration options. For more information, see Amazon ECS Container Agent Configuration in the Amazon Elastic Container Service Developer Guide .

logDriver -> (string)

The log driver to use for the container.
For tasks on AWS Fargate, the supported log drivers are awslogs , splunk , and awsfirelens .
For tasks hosted on Amazon EC2 instances, the supported log drivers are awslogs , fluentd , gelf , json-file , journald , logentries ,``syslog`` , splunk , and awsfirelens .
For more information about using the awslogs log driver, see Using the awslogs log driver in the Amazon Elastic Container Service Developer Guide .
For more information about using the awsfirelens log driver, see Custom log routing in the Amazon Elastic Container Service Developer Guide .

Note
If you have a custom driver that is not listed, you can fork the Amazon ECS container agent project that is available on GitHub and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, we do not currently provide support for running modified copies of this software.


options -> (map)

The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: sudo docker version --format '{{.Server.APIVersion}}'
key -> (string)
value -> (string)

secretOptions -> (list)

The secrets to pass to the log configuration. For more information, see Specifying Sensitive Data in the Amazon Elastic Container Service Developer Guide .
(structure)

An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:

To inject sensitive data into your containers as environment variables, use the secrets container definition parameter.
To reference sensitive information in the log configuration of a container, use the secretOptions container definition parameter.

For more information, see Specifying Sensitive Data in the Amazon Elastic Container Service Developer Guide .
name -> (string)

The name of the secret.

valueFrom -> (string)

The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.

Note
If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.





healthCheck -> (structure)

The container health check command and associated configuration parameters for the container. This parameter maps to HealthCheck in the Create a container section of the Docker Remote API and the HEALTHCHECK parameter of docker run .
command -> (list)

A string array representing the command that the container runs to determine if it is healthy. The string array must start with CMD to execute the command arguments directly, or CMD-SHELL to run the command with the containerâs default shell. For example:

[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]

An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see HealthCheck in the Create a container section of the Docker Remote API .
(string)

interval -> (integer)

The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.

timeout -> (integer)

The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.

retries -> (integer)

The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.

startPeriod -> (integer)

The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The startPeriod is disabled by default.

Note
If a health check succeeds within the startPeriod , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.



systemControls -> (list)

A list of namespaced kernel parameters to set in the container. This parameter maps to Sysctls in the Create a container section of the Docker Remote API and the --sysctl option to docker run .

Note
It is not recommended that you specify network-related systemControls parameters for multiple containers in a single task that also uses either the awsvpc or host network modes. For tasks that use the awsvpc network mode, the container that is started last determines which systemControls parameters take effect. For tasks that use the host network mode, it changes the container instanceâs namespaced kernel parameters as well as the containers.

(structure)

A list of namespaced kernel parameters to set in the container. This parameter maps to Sysctls in the Create a container section of the Docker Remote API and the --sysctl option to docker run .
It is not recommended that you specify network-related systemControls parameters for multiple containers in a single task that also uses either the awsvpc or host network mode for the following reasons:

For tasks that use the awsvpc network mode, if you set systemControls for any container, it applies to all containers in the task. If you set different systemControls for multiple containers in a single task, the container that is started last determines which systemControls take effect.
For tasks that use the host network mode, the systemControls parameter applies to the container instanceâs kernel parameter as well as that of all containers of any tasks running on that container instance.

namespace -> (string)

The namespaced kernel parameter for which to set a value .

value -> (string)

The value for the namespaced kernel parameter specified in namespace .



resourceRequirements -> (list)

The type and amount of a resource to assign to a container. The only supported resource is a GPU.
(structure)

The type and amount of a resource to assign to a container. The supported resource types are GPUs and Elastic Inference accelerators. For more information, see Working with GPUs on Amazon ECS or Working with Amazon Elastic Inference on Amazon ECS in the Amazon Elastic Container Service Developer Guide
value -> (string)

The value for the specified resource type.
If the GPU type is used, the value is the number of physical GPUs the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
If the InferenceAccelerator type is used, the value should match the deviceName for an  InferenceAccelerator specified in a task definition.

type -> (string)

The type of resource to assign to a container. The supported values are GPU or InferenceAccelerator .



firelensConfiguration -> (structure)

The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see Custom Log Routing in the Amazon Elastic Container Service Developer Guide .
type -> (string)

The log router to use. The valid values are fluentd or fluentbit .

options -> (map)

The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is "options":{"enable-ecs-log-metadata":"true|false","config-file-type:"s3|file","config-file-value":"arn:aws:s3:::mybucket/fluent.conf|filepath"} . For more information, see Creating a Task Definition that Uses a FireLens Configuration in the Amazon Elastic Container Service Developer Guide .
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecs", "register-task-definition", "family", "container-definitions", add_option_dict)
