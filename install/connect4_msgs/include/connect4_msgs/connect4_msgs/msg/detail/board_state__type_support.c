// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "connect4_msgs/msg/detail/board_state__rosidl_typesupport_introspection_c.h"
#include "connect4_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "connect4_msgs/msg/detail/board_state__functions.h"
#include "connect4_msgs/msg/detail/board_state__struct.h"


// Include directives for member types
// Member `cells`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  connect4_msgs__msg__BoardState__init(message_memory);
}

void connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_fini_function(void * message_memory)
{
  connect4_msgs__msg__BoardState__fini(message_memory);
}

size_t connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__size_function__BoardState__cells(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_const_function__BoardState__cells(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_function__BoardState__cells(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__fetch_function__BoardState__cells(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_const_function__BoardState__cells(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__assign_function__BoardState__cells(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_function__BoardState__cells(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__resize_function__BoardState__cells(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_member_array[1] = {
  {
    "cells",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(connect4_msgs__msg__BoardState, cells),  // bytes offset in struct
    NULL,  // default value
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__size_function__BoardState__cells,  // size() function pointer
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_const_function__BoardState__cells,  // get_const(index) function pointer
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__get_function__BoardState__cells,  // get(index) function pointer
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__fetch_function__BoardState__cells,  // fetch(index, &value) function pointer
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__assign_function__BoardState__cells,  // assign(index, value) function pointer
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__resize_function__BoardState__cells  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_members = {
  "connect4_msgs__msg",  // message namespace
  "BoardState",  // message name
  1,  // number of fields
  sizeof(connect4_msgs__msg__BoardState),
  false,  // has_any_key_member_
  connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_member_array,  // message members
  connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_init_function,  // function to initialize message memory (memory has to be allocated)
  connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_type_support_handle = {
  0,
  &connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_members,
  get_message_typesupport_handle_function,
  &connect4_msgs__msg__BoardState__get_type_hash,
  &connect4_msgs__msg__BoardState__get_type_description,
  &connect4_msgs__msg__BoardState__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_connect4_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, connect4_msgs, msg, BoardState)() {
  if (!connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_type_support_handle.typesupport_identifier) {
    connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &connect4_msgs__msg__BoardState__rosidl_typesupport_introspection_c__BoardState_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
