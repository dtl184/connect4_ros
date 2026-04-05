// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice
#ifndef CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "connect4_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "connect4_msgs/msg/detail/board_state__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
bool cdr_serialize_connect4_msgs__msg__BoardState(
  const connect4_msgs__msg__BoardState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
bool cdr_deserialize_connect4_msgs__msg__BoardState(
  eprosima::fastcdr::Cdr &,
  connect4_msgs__msg__BoardState * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
size_t get_serialized_size_connect4_msgs__msg__BoardState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
size_t max_serialized_size_connect4_msgs__msg__BoardState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
bool cdr_serialize_key_connect4_msgs__msg__BoardState(
  const connect4_msgs__msg__BoardState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
size_t get_serialized_size_key_connect4_msgs__msg__BoardState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
size_t max_serialized_size_key_connect4_msgs__msg__BoardState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_connect4_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, connect4_msgs, msg, BoardState)();

#ifdef __cplusplus
}
#endif

#endif  // CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
