// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice

#include "connect4_msgs/msg/detail/board_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
const rosidl_type_hash_t *
connect4_msgs__msg__BoardState__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x24, 0xe7, 0x16, 0x04, 0xad, 0xd7, 0x8c, 0x44,
      0x48, 0xcb, 0xb6, 0x87, 0x08, 0xd5, 0x7b, 0xcb,
      0xbe, 0xd0, 0x2f, 0xe7, 0x88, 0x41, 0x53, 0xbe,
      0x95, 0xd4, 0x24, 0x59, 0x67, 0xc2, 0x93, 0x29,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char connect4_msgs__msg__BoardState__TYPE_NAME[] = "connect4_msgs/msg/BoardState";

// Define type names, field names, and default values
static char connect4_msgs__msg__BoardState__FIELD_NAME__cells[] = "cells";

static rosidl_runtime_c__type_description__Field connect4_msgs__msg__BoardState__FIELDS[] = {
  {
    {connect4_msgs__msg__BoardState__FIELD_NAME__cells, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
connect4_msgs__msg__BoardState__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {connect4_msgs__msg__BoardState__TYPE_NAME, 28, 28},
      {connect4_msgs__msg__BoardState__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int32[] cells";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
connect4_msgs__msg__BoardState__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {connect4_msgs__msg__BoardState__TYPE_NAME, 28, 28},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 14, 14},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
connect4_msgs__msg__BoardState__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *connect4_msgs__msg__BoardState__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
