// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from connect4_msgs:action/ResetBoard.idl
// generated code does not contain a copyright notice

#ifndef CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__STRUCT_H_
#define CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'final_board_state'
#include "connect4_msgs/msg/detail/board_state__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_Goal
{
  connect4_msgs__msg__BoardState final_board_state;
} connect4_msgs__action__ResetBoard_Goal;

// Struct for a sequence of connect4_msgs__action__ResetBoard_Goal.
typedef struct connect4_msgs__action__ResetBoard_Goal__Sequence
{
  connect4_msgs__action__ResetBoard_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_Result
{
  bool success;
  rosidl_runtime_c__String message;
} connect4_msgs__action__ResetBoard_Result;

// Struct for a sequence of connect4_msgs__action__ResetBoard_Result.
typedef struct connect4_msgs__action__ResetBoard_Result__Sequence
{
  connect4_msgs__action__ResetBoard_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'status'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_Feedback
{
  rosidl_runtime_c__String status;
} connect4_msgs__action__ResetBoard_Feedback;

// Struct for a sequence of connect4_msgs__action__ResetBoard_Feedback.
typedef struct connect4_msgs__action__ResetBoard_Feedback__Sequence
{
  connect4_msgs__action__ResetBoard_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "connect4_msgs/action/detail/reset_board__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  connect4_msgs__action__ResetBoard_Goal goal;
} connect4_msgs__action__ResetBoard_SendGoal_Request;

// Struct for a sequence of connect4_msgs__action__ResetBoard_SendGoal_Request.
typedef struct connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence
{
  connect4_msgs__action__ResetBoard_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} connect4_msgs__action__ResetBoard_SendGoal_Response;

// Struct for a sequence of connect4_msgs__action__ResetBoard_SendGoal_Response.
typedef struct connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence
{
  connect4_msgs__action__ResetBoard_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} connect4_msgs__action__ResetBoard_GetResult_Request;

// Struct for a sequence of connect4_msgs__action__ResetBoard_GetResult_Request.
typedef struct connect4_msgs__action__ResetBoard_GetResult_Request__Sequence
{
  connect4_msgs__action__ResetBoard_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "connect4_msgs/action/detail/reset_board__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_GetResult_Response
{
  int8_t status;
  connect4_msgs__action__ResetBoard_Result result;
} connect4_msgs__action__ResetBoard_GetResult_Response;

// Struct for a sequence of connect4_msgs__action__ResetBoard_GetResult_Response.
typedef struct connect4_msgs__action__ResetBoard_GetResult_Response__Sequence
{
  connect4_msgs__action__ResetBoard_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "connect4_msgs/action/detail/reset_board__struct.h"

/// Struct defined in action/ResetBoard in the package connect4_msgs.
typedef struct connect4_msgs__action__ResetBoard_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  connect4_msgs__action__ResetBoard_Feedback feedback;
} connect4_msgs__action__ResetBoard_FeedbackMessage;

// Struct for a sequence of connect4_msgs__action__ResetBoard_FeedbackMessage.
typedef struct connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence
{
  connect4_msgs__action__ResetBoard_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__STRUCT_H_
