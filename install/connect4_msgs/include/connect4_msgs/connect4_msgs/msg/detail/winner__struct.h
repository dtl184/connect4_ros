// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "connect4_msgs/msg/winner.h"


#ifndef CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_H_
#define CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Winner in the package connect4_msgs.
typedef struct connect4_msgs__msg__Winner
{
  int32_t winner;
} connect4_msgs__msg__Winner;

// Struct for a sequence of connect4_msgs__msg__Winner.
typedef struct connect4_msgs__msg__Winner__Sequence
{
  connect4_msgs__msg__Winner * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__msg__Winner__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_H_
