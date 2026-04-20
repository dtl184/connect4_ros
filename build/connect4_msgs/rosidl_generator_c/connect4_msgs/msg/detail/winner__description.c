// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice

#include "connect4_msgs/msg/detail/winner__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
const rosidl_type_hash_t *
connect4_msgs__msg__Winner__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xea, 0xd7, 0x42, 0xd6, 0xf2, 0xfc, 0xc9, 0x6d,
      0x70, 0x95, 0x29, 0xd9, 0xd8, 0x32, 0x6c, 0xe7,
      0xb7, 0x69, 0xa6, 0x81, 0xfe, 0x23, 0x7a, 0xb9,
      0xef, 0x4f, 0xcd, 0x89, 0x13, 0x9a, 0x85, 0xdc,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char connect4_msgs__msg__Winner__TYPE_NAME[] = "connect4_msgs/msg/Winner";

// Define type names, field names, and default values
static char connect4_msgs__msg__Winner__FIELD_NAME__winner[] = "winner";

static rosidl_runtime_c__type_description__Field connect4_msgs__msg__Winner__FIELDS[] = {
  {
    {connect4_msgs__msg__Winner__FIELD_NAME__winner, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
connect4_msgs__msg__Winner__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {connect4_msgs__msg__Winner__TYPE_NAME, 24, 24},
      {connect4_msgs__msg__Winner__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int32 winner";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
connect4_msgs__msg__Winner__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {connect4_msgs__msg__Winner__TYPE_NAME, 24, 24},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 13, 13},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
connect4_msgs__msg__Winner__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *connect4_msgs__msg__Winner__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
