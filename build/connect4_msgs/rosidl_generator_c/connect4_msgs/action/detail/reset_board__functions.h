// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from connect4_msgs:action/ResetBoard.idl
// generated code does not contain a copyright notice

#ifndef CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__FUNCTIONS_H_
#define CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "connect4_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "connect4_msgs/action/detail/reset_board__struct.h"

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_Goal
 * )) before or use
 * connect4_msgs__action__ResetBoard_Goal__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__init(connect4_msgs__action__ResetBoard_Goal * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Goal__fini(connect4_msgs__action__ResetBoard_Goal * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_Goal__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Goal *
connect4_msgs__action__ResetBoard_Goal__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Goal__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Goal__destroy(connect4_msgs__action__ResetBoard_Goal * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__are_equal(const connect4_msgs__action__ResetBoard_Goal * lhs, const connect4_msgs__action__ResetBoard_Goal * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__copy(
  const connect4_msgs__action__ResetBoard_Goal * input,
  connect4_msgs__action__ResetBoard_Goal * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_Goal__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__Sequence__init(connect4_msgs__action__ResetBoard_Goal__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Goal__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Goal__Sequence__fini(connect4_msgs__action__ResetBoard_Goal__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_Goal__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Goal__Sequence *
connect4_msgs__action__ResetBoard_Goal__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Goal__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Goal__Sequence__destroy(connect4_msgs__action__ResetBoard_Goal__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__Sequence__are_equal(const connect4_msgs__action__ResetBoard_Goal__Sequence * lhs, const connect4_msgs__action__ResetBoard_Goal__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Goal__Sequence__copy(
  const connect4_msgs__action__ResetBoard_Goal__Sequence * input,
  connect4_msgs__action__ResetBoard_Goal__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_Result
 * )) before or use
 * connect4_msgs__action__ResetBoard_Result__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__init(connect4_msgs__action__ResetBoard_Result * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Result__fini(connect4_msgs__action__ResetBoard_Result * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_Result__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Result *
connect4_msgs__action__ResetBoard_Result__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Result__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Result__destroy(connect4_msgs__action__ResetBoard_Result * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__are_equal(const connect4_msgs__action__ResetBoard_Result * lhs, const connect4_msgs__action__ResetBoard_Result * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__copy(
  const connect4_msgs__action__ResetBoard_Result * input,
  connect4_msgs__action__ResetBoard_Result * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_Result__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__Sequence__init(connect4_msgs__action__ResetBoard_Result__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Result__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Result__Sequence__fini(connect4_msgs__action__ResetBoard_Result__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_Result__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Result__Sequence *
connect4_msgs__action__ResetBoard_Result__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Result__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Result__Sequence__destroy(connect4_msgs__action__ResetBoard_Result__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__Sequence__are_equal(const connect4_msgs__action__ResetBoard_Result__Sequence * lhs, const connect4_msgs__action__ResetBoard_Result__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Result__Sequence__copy(
  const connect4_msgs__action__ResetBoard_Result__Sequence * input,
  connect4_msgs__action__ResetBoard_Result__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_Feedback
 * )) before or use
 * connect4_msgs__action__ResetBoard_Feedback__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__init(connect4_msgs__action__ResetBoard_Feedback * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Feedback__fini(connect4_msgs__action__ResetBoard_Feedback * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_Feedback__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Feedback *
connect4_msgs__action__ResetBoard_Feedback__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Feedback__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Feedback__destroy(connect4_msgs__action__ResetBoard_Feedback * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__are_equal(const connect4_msgs__action__ResetBoard_Feedback * lhs, const connect4_msgs__action__ResetBoard_Feedback * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__copy(
  const connect4_msgs__action__ResetBoard_Feedback * input,
  connect4_msgs__action__ResetBoard_Feedback * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_Feedback__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__Sequence__init(connect4_msgs__action__ResetBoard_Feedback__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Feedback__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Feedback__Sequence__fini(connect4_msgs__action__ResetBoard_Feedback__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_Feedback__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_Feedback__Sequence *
connect4_msgs__action__ResetBoard_Feedback__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_Feedback__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_Feedback__Sequence__destroy(connect4_msgs__action__ResetBoard_Feedback__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__Sequence__are_equal(const connect4_msgs__action__ResetBoard_Feedback__Sequence * lhs, const connect4_msgs__action__ResetBoard_Feedback__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_Feedback__Sequence__copy(
  const connect4_msgs__action__ResetBoard_Feedback__Sequence * input,
  connect4_msgs__action__ResetBoard_Feedback__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_SendGoal_Request
 * )) before or use
 * connect4_msgs__action__ResetBoard_SendGoal_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__init(connect4_msgs__action__ResetBoard_SendGoal_Request * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Request__fini(connect4_msgs__action__ResetBoard_SendGoal_Request * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_SendGoal_Request *
connect4_msgs__action__ResetBoard_SendGoal_Request__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Request__destroy(connect4_msgs__action__ResetBoard_SendGoal_Request * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__are_equal(const connect4_msgs__action__ResetBoard_SendGoal_Request * lhs, const connect4_msgs__action__ResetBoard_SendGoal_Request * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__copy(
  const connect4_msgs__action__ResetBoard_SendGoal_Request * input,
  connect4_msgs__action__ResetBoard_SendGoal_Request * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__init(connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__fini(connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence *
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__destroy(connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__are_equal(const connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * lhs, const connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__copy(
  const connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * input,
  connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_SendGoal_Response
 * )) before or use
 * connect4_msgs__action__ResetBoard_SendGoal_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__init(connect4_msgs__action__ResetBoard_SendGoal_Response * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Response__fini(connect4_msgs__action__ResetBoard_SendGoal_Response * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_SendGoal_Response *
connect4_msgs__action__ResetBoard_SendGoal_Response__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Response__destroy(connect4_msgs__action__ResetBoard_SendGoal_Response * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__are_equal(const connect4_msgs__action__ResetBoard_SendGoal_Response * lhs, const connect4_msgs__action__ResetBoard_SendGoal_Response * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__copy(
  const connect4_msgs__action__ResetBoard_SendGoal_Response * input,
  connect4_msgs__action__ResetBoard_SendGoal_Response * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__init(connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__fini(connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence *
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__destroy(connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__are_equal(const connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * lhs, const connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__copy(
  const connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * input,
  connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_GetResult_Request
 * )) before or use
 * connect4_msgs__action__ResetBoard_GetResult_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__init(connect4_msgs__action__ResetBoard_GetResult_Request * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Request__fini(connect4_msgs__action__ResetBoard_GetResult_Request * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_GetResult_Request *
connect4_msgs__action__ResetBoard_GetResult_Request__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Request__destroy(connect4_msgs__action__ResetBoard_GetResult_Request * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__are_equal(const connect4_msgs__action__ResetBoard_GetResult_Request * lhs, const connect4_msgs__action__ResetBoard_GetResult_Request * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__copy(
  const connect4_msgs__action__ResetBoard_GetResult_Request * input,
  connect4_msgs__action__ResetBoard_GetResult_Request * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__init(connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__fini(connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence *
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__destroy(connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__are_equal(const connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * lhs, const connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__copy(
  const connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * input,
  connect4_msgs__action__ResetBoard_GetResult_Request__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_GetResult_Response
 * )) before or use
 * connect4_msgs__action__ResetBoard_GetResult_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__init(connect4_msgs__action__ResetBoard_GetResult_Response * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Response__fini(connect4_msgs__action__ResetBoard_GetResult_Response * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_GetResult_Response *
connect4_msgs__action__ResetBoard_GetResult_Response__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Response__destroy(connect4_msgs__action__ResetBoard_GetResult_Response * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__are_equal(const connect4_msgs__action__ResetBoard_GetResult_Response * lhs, const connect4_msgs__action__ResetBoard_GetResult_Response * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__copy(
  const connect4_msgs__action__ResetBoard_GetResult_Response * input,
  connect4_msgs__action__ResetBoard_GetResult_Response * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__init(connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__fini(connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence *
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__destroy(connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__are_equal(const connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * lhs, const connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__copy(
  const connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * input,
  connect4_msgs__action__ResetBoard_GetResult_Response__Sequence * output);

/// Initialize action/ResetBoard message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * connect4_msgs__action__ResetBoard_FeedbackMessage
 * )) before or use
 * connect4_msgs__action__ResetBoard_FeedbackMessage__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__init(connect4_msgs__action__ResetBoard_FeedbackMessage * msg);

/// Finalize action/ResetBoard message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_FeedbackMessage__fini(connect4_msgs__action__ResetBoard_FeedbackMessage * msg);

/// Create action/ResetBoard message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_FeedbackMessage *
connect4_msgs__action__ResetBoard_FeedbackMessage__create();

/// Destroy action/ResetBoard message.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_FeedbackMessage__destroy(connect4_msgs__action__ResetBoard_FeedbackMessage * msg);

/// Check for action/ResetBoard message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__are_equal(const connect4_msgs__action__ResetBoard_FeedbackMessage * lhs, const connect4_msgs__action__ResetBoard_FeedbackMessage * rhs);

/// Copy a action/ResetBoard message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__copy(
  const connect4_msgs__action__ResetBoard_FeedbackMessage * input,
  connect4_msgs__action__ResetBoard_FeedbackMessage * output);

/// Initialize array of action/ResetBoard messages.
/**
 * It allocates the memory for the number of elements and calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__init(connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * array, size_t size);

/// Finalize array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__fini(connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * array);

/// Create array of action/ResetBoard messages.
/**
 * It allocates the memory for the array and calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence *
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__create(size_t size);

/// Destroy array of action/ResetBoard messages.
/**
 * It calls
 * connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
void
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__destroy(connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * array);

/// Check for action/ResetBoard message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__are_equal(const connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * lhs, const connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * rhs);

/// Copy an array of action/ResetBoard messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_connect4_msgs
bool
connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__copy(
  const connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * input,
  connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__FUNCTIONS_H_
