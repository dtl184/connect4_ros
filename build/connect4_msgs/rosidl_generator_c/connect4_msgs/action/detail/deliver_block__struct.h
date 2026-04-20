// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from connect4_msgs:action/DeliverBlock.idl
// generated code does not contain a copyright notice

#ifndef CONNECT4_MSGS__ACTION__DETAIL__DELIVER_BLOCK__STRUCT_H_
#define CONNECT4_MSGS__ACTION__DETAIL__DELIVER_BLOCK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_Goal
{
  int32_t player;
} connect4_msgs__action__DeliverBlock_Goal;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_Goal.
typedef struct connect4_msgs__action__DeliverBlock_Goal__Sequence
{
  connect4_msgs__action__DeliverBlock_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_Result
{
  bool success;
  rosidl_runtime_c__String message;
} connect4_msgs__action__DeliverBlock_Result;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_Result.
typedef struct connect4_msgs__action__DeliverBlock_Result__Sequence
{
  connect4_msgs__action__DeliverBlock_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'status'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_Feedback
{
  rosidl_runtime_c__String status;
} connect4_msgs__action__DeliverBlock_Feedback;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_Feedback.
typedef struct connect4_msgs__action__DeliverBlock_Feedback__Sequence
{
  connect4_msgs__action__DeliverBlock_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "connect4_msgs/action/detail/deliver_block__struct.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  connect4_msgs__action__DeliverBlock_Goal goal;
} connect4_msgs__action__DeliverBlock_SendGoal_Request;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_SendGoal_Request.
typedef struct connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence
{
  connect4_msgs__action__DeliverBlock_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} connect4_msgs__action__DeliverBlock_SendGoal_Response;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_SendGoal_Response.
typedef struct connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence
{
  connect4_msgs__action__DeliverBlock_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} connect4_msgs__action__DeliverBlock_GetResult_Request;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_GetResult_Request.
typedef struct connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence
{
  connect4_msgs__action__DeliverBlock_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "connect4_msgs/action/detail/deliver_block__struct.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_GetResult_Response
{
  int8_t status;
  connect4_msgs__action__DeliverBlock_Result result;
} connect4_msgs__action__DeliverBlock_GetResult_Response;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_GetResult_Response.
typedef struct connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence
{
  connect4_msgs__action__DeliverBlock_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "connect4_msgs/action/detail/deliver_block__struct.h"

/// Struct defined in action/DeliverBlock in the package connect4_msgs.
typedef struct connect4_msgs__action__DeliverBlock_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  connect4_msgs__action__DeliverBlock_Feedback feedback;
} connect4_msgs__action__DeliverBlock_FeedbackMessage;

// Struct for a sequence of connect4_msgs__action__DeliverBlock_FeedbackMessage.
typedef struct connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence
{
  connect4_msgs__action__DeliverBlock_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONNECT4_MSGS__ACTION__DETAIL__DELIVER_BLOCK__STRUCT_H_
