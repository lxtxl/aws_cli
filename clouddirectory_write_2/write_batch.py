#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-write.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
    # operations : A list of operations that are part of the batch.
(structure)

Represents the output of a BatchWrite operation.
CreateObject -> (structure)

Creates an object.
SchemaFacet -> (list)

A list of FacetArns that will be associated with the object. For more information, see  arns .
(structure)

A facet.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.



ObjectAttributeList -> (list)

An attribute map, which contains an attribute ARN as the key and attribute value as the map value.
(structure)

The combination of an attribute key and an attribute value.
Key -> (structure)

The key of the attribute.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


Value -> (structure)

The value of the attribute.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.




ParentReference -> (structure)

If specified, the parent reference to which this object will be attached.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



LinkName -> (string)

The name of the link.

BatchReferenceName -> (string)

The batch reference name. See Transaction Support for more information.


AttachObject -> (structure)

Attaches an object to a  Directory .
ParentReference -> (structure)

The parent object reference.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



ChildReference -> (structure)

The child object reference that is to be attached to the object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



LinkName -> (string)

The name of the link.


DetachObject -> (structure)

Detaches an object from a  Directory .
ParentReference -> (structure)

Parent reference from which the object with the specified link name is detached.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



LinkName -> (string)

The name of the link.

BatchReferenceName -> (string)

The batch reference name. See Transaction Support for more information.


UpdateObjectAttributes -> (structure)

Updates a given objectâs attributes.
ObjectReference -> (structure)

Reference that identifies the object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



AttributeUpdates -> (list)

Attributes update structure.
(structure)

Structure that contains attribute update information.
ObjectAttributeKey -> (structure)

The key of the attribute being updated.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


ObjectAttributeAction -> (structure)

The action to perform as part of the attribute update.
ObjectAttributeActionType -> (string)

A type that can be either Update or Delete .

ObjectAttributeUpdateValue -> (structure)

The value that you want to update to.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.






DeleteObject -> (structure)

Deletes an object in a  Directory .
ObjectReference -> (structure)

The reference that identifies the object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




AddFacetToObject -> (structure)

A batch operation that adds a facet to an object.
SchemaFacet -> (structure)

Represents the facet being added to the object.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.


ObjectAttributeList -> (list)

The attributes to set on the object.
(structure)

The combination of an attribute key and an attribute value.
Key -> (structure)

The key of the attribute.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


Value -> (structure)

The value of the attribute.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.




ObjectReference -> (structure)

A reference to the object being mutated.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




RemoveFacetFromObject -> (structure)

A batch operation that removes a facet from an object.
SchemaFacet -> (structure)

The facet to remove from the object.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.


ObjectReference -> (structure)

A reference to the object whose facet will be removed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




AttachPolicy -> (structure)

Attaches a policy object to a regular object. An object can have a limited number of attached policies.
PolicyReference -> (structure)

The reference that is associated with the policy object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



ObjectReference -> (structure)

The reference that identifies the object to which the policy will be attached.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




DetachPolicy -> (structure)

Detaches a policy from a  Directory .
PolicyReference -> (structure)

Reference that identifies the policy object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



ObjectReference -> (structure)

Reference that identifies the object whose policy object will be detached.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




CreateIndex -> (structure)

Creates an index object. See Indexing and search for more information.
OrderedIndexedAttributeList -> (list)

Specifies the attributes that should be indexed on. Currently only a single attribute is supported.
(structure)

A unique identifier for an attribute.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.



IsUnique -> (boolean)

Indicates whether the attribute that is being indexed has unique values or not.

ParentReference -> (structure)

A reference to the parent object that contains the index object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



LinkName -> (string)

The name of the link between the parent object and the index object.

BatchReferenceName -> (string)

The batch reference name. See Transaction Support for more information.


AttachToIndex -> (structure)

Attaches the specified object to the specified index.
IndexReference -> (structure)

A reference to the index that you are attaching the object to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetReference -> (structure)

A reference to the object that you are attaching to the index.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




DetachFromIndex -> (structure)

Detaches the specified object from the specified index.
IndexReference -> (structure)

A reference to the index object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetReference -> (structure)

A reference to the object being detached from the index.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




AttachTypedLink -> (structure)

Attaches a typed link to a specified source and target object. For more information, see Typed Links .
SourceObjectReference -> (structure)

Identifies the source object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetObjectReference -> (structure)

Identifies the target object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


Attributes -> (list)

A set of attributes that are associated with the typed link.
(structure)

Identifies the attribute name and value for a typed link.
AttributeName -> (string)

The attribute name of the typed link.

Value -> (structure)

The value for the typed link.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





DetachTypedLink -> (structure)

Detaches a typed link from a specified source and target object. For more information, see Typed Links .
TypedLinkSpecifier -> (structure)

Used to accept a typed link specifier as input.
TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


SourceObjectReference -> (structure)

Identifies the source object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetObjectReference -> (structure)

Identifies the target object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



IdentityAttributeValues -> (list)

Identifies the attribute value to update.
(structure)

Identifies the attribute name and value for a typed link.
AttributeName -> (string)

The attribute name of the typed link.

Value -> (structure)

The value for the typed link.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.






UpdateLinkAttributes -> (structure)

Updates a given objectâs attributes.
TypedLinkSpecifier -> (structure)

Allows a typed link specifier to be accepted as input.
TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


SourceObjectReference -> (structure)

Identifies the source object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetObjectReference -> (structure)

Identifies the target object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



IdentityAttributeValues -> (list)

Identifies the attribute value to update.
(structure)

Identifies the attribute name and value for a typed link.
AttributeName -> (string)

The attribute name of the typed link.

Value -> (structure)

The value for the typed link.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





AttributeUpdates -> (list)

The attributes update structure.
(structure)

Structure that contains attribute update information.
AttributeKey -> (structure)

The key of the attribute being updated.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


AttributeAction -> (structure)

The action to perform as part of the attribute update.
AttributeActionType -> (string)

A type that can be either UPDATE_OR_CREATE or DELETE .

AttributeUpdateValue -> (structure)

The value that you want to update to.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "batch-write", "directory-arn", "operations", add_option_dict)
