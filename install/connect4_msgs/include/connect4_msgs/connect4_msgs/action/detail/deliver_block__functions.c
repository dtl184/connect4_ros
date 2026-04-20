// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from connect4_msgs:action/DeliverBlock.idl
// generated code does not contain a copyright notice
#include "connect4_msgs/action/detail/deliver_block__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
connect4_msgs__action__DeliverBlock_Goal__init(connect4_msgs__action__DeliverBlock_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // player
  return true;
}

void
connect4_msgs__action__DeliverBlock_Goal__fini(connect4_msgs__action__DeliverBlock_Goal * msg)
{
  if (!msg) {
    return;
  }
  // player
}

bool
connect4_msgs__action__DeliverBlock_Goal__are_equal(const connect4_msgs__action__DeliverBlock_Goal * lhs, const connect4_msgs__action__DeliverBlock_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // player
  if (lhs->player != rhs->player) {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Goal__copy(
  const connect4_msgs__action__DeliverBlock_Goal * input,
  connect4_msgs__action__DeliverBlock_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // player
  output->player = input->player;
  return true;
}

connect4_msgs__action__DeliverBlock_Goal *
connect4_msgs__action__DeliverBlock_Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Goal * msg = (connect4_msgs__action__DeliverBlock_Goal *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_Goal));
  bool success = connect4_msgs__action__DeliverBlock_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_Goal__destroy(connect4_msgs__action__DeliverBlock_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_Goal__Sequence__init(connect4_msgs__action__DeliverBlock_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Goal * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_Goal *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_Goal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_Goal__Sequence__fini(connect4_msgs__action__DeliverBlock_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_Goal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_Goal__Sequence *
connect4_msgs__action__DeliverBlock_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Goal__Sequence * array = (connect4_msgs__action__DeliverBlock_Goal__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_Goal__Sequence__destroy(connect4_msgs__action__DeliverBlock_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_Goal__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_Goal__Sequence * lhs, const connect4_msgs__action__DeliverBlock_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Goal__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_Goal__Sequence * input,
  connect4_msgs__action__DeliverBlock_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_Goal * data =
      (connect4_msgs__action__DeliverBlock_Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

bool
connect4_msgs__action__DeliverBlock_Result__init(connect4_msgs__action__DeliverBlock_Result * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    connect4_msgs__action__DeliverBlock_Result__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_Result__fini(connect4_msgs__action__DeliverBlock_Result * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
connect4_msgs__action__DeliverBlock_Result__are_equal(const connect4_msgs__action__DeliverBlock_Result * lhs, const connect4_msgs__action__DeliverBlock_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Result__copy(
  const connect4_msgs__action__DeliverBlock_Result * input,
  connect4_msgs__action__DeliverBlock_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_Result *
connect4_msgs__action__DeliverBlock_Result__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Result * msg = (connect4_msgs__action__DeliverBlock_Result *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_Result));
  bool success = connect4_msgs__action__DeliverBlock_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_Result__destroy(connect4_msgs__action__DeliverBlock_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_Result__Sequence__init(connect4_msgs__action__DeliverBlock_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Result * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_Result *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_Result__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_Result__Sequence__fini(connect4_msgs__action__DeliverBlock_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_Result__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_Result__Sequence *
connect4_msgs__action__DeliverBlock_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Result__Sequence * array = (connect4_msgs__action__DeliverBlock_Result__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_Result__Sequence__destroy(connect4_msgs__action__DeliverBlock_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_Result__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_Result__Sequence * lhs, const connect4_msgs__action__DeliverBlock_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Result__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_Result__Sequence * input,
  connect4_msgs__action__DeliverBlock_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_Result);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_Result * data =
      (connect4_msgs__action__DeliverBlock_Result *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_Result__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_Result__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `status`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
connect4_msgs__action__DeliverBlock_Feedback__init(connect4_msgs__action__DeliverBlock_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    connect4_msgs__action__DeliverBlock_Feedback__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_Feedback__fini(connect4_msgs__action__DeliverBlock_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // status
  rosidl_runtime_c__String__fini(&msg->status);
}

bool
connect4_msgs__action__DeliverBlock_Feedback__are_equal(const connect4_msgs__action__DeliverBlock_Feedback * lhs, const connect4_msgs__action__DeliverBlock_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Feedback__copy(
  const connect4_msgs__action__DeliverBlock_Feedback * input,
  connect4_msgs__action__DeliverBlock_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_Feedback *
connect4_msgs__action__DeliverBlock_Feedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Feedback * msg = (connect4_msgs__action__DeliverBlock_Feedback *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_Feedback));
  bool success = connect4_msgs__action__DeliverBlock_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_Feedback__destroy(connect4_msgs__action__DeliverBlock_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_Feedback__Sequence__init(connect4_msgs__action__DeliverBlock_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Feedback * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_Feedback *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_Feedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_Feedback__Sequence__fini(connect4_msgs__action__DeliverBlock_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_Feedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_Feedback__Sequence *
connect4_msgs__action__DeliverBlock_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_Feedback__Sequence * array = (connect4_msgs__action__DeliverBlock_Feedback__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_Feedback__Sequence__destroy(connect4_msgs__action__DeliverBlock_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_Feedback__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_Feedback__Sequence * lhs, const connect4_msgs__action__DeliverBlock_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_Feedback__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_Feedback__Sequence * input,
  connect4_msgs__action__DeliverBlock_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_Feedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_Feedback * data =
      (connect4_msgs__action__DeliverBlock_Feedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_Feedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_Feedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "connect4_msgs/action/detail/deliver_block__functions.h"

bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__init(connect4_msgs__action__DeliverBlock_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!connect4_msgs__action__DeliverBlock_Goal__init(&msg->goal)) {
    connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(connect4_msgs__action__DeliverBlock_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  connect4_msgs__action__DeliverBlock_Goal__fini(&msg->goal);
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__are_equal(const connect4_msgs__action__DeliverBlock_SendGoal_Request * lhs, const connect4_msgs__action__DeliverBlock_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!connect4_msgs__action__DeliverBlock_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__copy(
  const connect4_msgs__action__DeliverBlock_SendGoal_Request * input,
  connect4_msgs__action__DeliverBlock_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!connect4_msgs__action__DeliverBlock_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_SendGoal_Request *
connect4_msgs__action__DeliverBlock_SendGoal_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Request * msg = (connect4_msgs__action__DeliverBlock_SendGoal_Request *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Request));
  bool success = connect4_msgs__action__DeliverBlock_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Request__destroy(connect4_msgs__action__DeliverBlock_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__init(connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Request * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_SendGoal_Request *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__fini(connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence *
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * array = (connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__destroy(connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * lhs, const connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * input,
  connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_SendGoal_Request * data =
      (connect4_msgs__action__DeliverBlock_SendGoal_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_SendGoal_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_SendGoal_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__init(connect4_msgs__action__DeliverBlock_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(connect4_msgs__action__DeliverBlock_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__are_equal(const connect4_msgs__action__DeliverBlock_SendGoal_Response * lhs, const connect4_msgs__action__DeliverBlock_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__copy(
  const connect4_msgs__action__DeliverBlock_SendGoal_Response * input,
  connect4_msgs__action__DeliverBlock_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_SendGoal_Response *
connect4_msgs__action__DeliverBlock_SendGoal_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Response * msg = (connect4_msgs__action__DeliverBlock_SendGoal_Response *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Response));
  bool success = connect4_msgs__action__DeliverBlock_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Response__destroy(connect4_msgs__action__DeliverBlock_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__init(connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Response * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_SendGoal_Response *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__fini(connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence *
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * array = (connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__destroy(connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * lhs, const connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * input,
  connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_SendGoal_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_SendGoal_Response * data =
      (connect4_msgs__action__DeliverBlock_SendGoal_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_SendGoal_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_SendGoal_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
connect4_msgs__action__DeliverBlock_GetResult_Request__init(connect4_msgs__action__DeliverBlock_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    connect4_msgs__action__DeliverBlock_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Request__fini(connect4_msgs__action__DeliverBlock_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Request__are_equal(const connect4_msgs__action__DeliverBlock_GetResult_Request * lhs, const connect4_msgs__action__DeliverBlock_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Request__copy(
  const connect4_msgs__action__DeliverBlock_GetResult_Request * input,
  connect4_msgs__action__DeliverBlock_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_GetResult_Request *
connect4_msgs__action__DeliverBlock_GetResult_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Request * msg = (connect4_msgs__action__DeliverBlock_GetResult_Request *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_GetResult_Request));
  bool success = connect4_msgs__action__DeliverBlock_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Request__destroy(connect4_msgs__action__DeliverBlock_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__init(connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Request * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_GetResult_Request *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_GetResult_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__fini(connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_GetResult_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence *
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * array = (connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__destroy(connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * lhs, const connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * input,
  connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_GetResult_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_GetResult_Request * data =
      (connect4_msgs__action__DeliverBlock_GetResult_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_GetResult_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_GetResult_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "connect4_msgs/action/detail/deliver_block__functions.h"

bool
connect4_msgs__action__DeliverBlock_GetResult_Response__init(connect4_msgs__action__DeliverBlock_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!connect4_msgs__action__DeliverBlock_Result__init(&msg->result)) {
    connect4_msgs__action__DeliverBlock_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Response__fini(connect4_msgs__action__DeliverBlock_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  connect4_msgs__action__DeliverBlock_Result__fini(&msg->result);
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Response__are_equal(const connect4_msgs__action__DeliverBlock_GetResult_Response * lhs, const connect4_msgs__action__DeliverBlock_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!connect4_msgs__action__DeliverBlock_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Response__copy(
  const connect4_msgs__action__DeliverBlock_GetResult_Response * input,
  connect4_msgs__action__DeliverBlock_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!connect4_msgs__action__DeliverBlock_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_GetResult_Response *
connect4_msgs__action__DeliverBlock_GetResult_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Response * msg = (connect4_msgs__action__DeliverBlock_GetResult_Response *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_GetResult_Response));
  bool success = connect4_msgs__action__DeliverBlock_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Response__destroy(connect4_msgs__action__DeliverBlock_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__init(connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Response * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_GetResult_Response *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_GetResult_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__fini(connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_GetResult_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence *
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * array = (connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__destroy(connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * lhs, const connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * input,
  connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_GetResult_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_GetResult_Response * data =
      (connect4_msgs__action__DeliverBlock_GetResult_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_GetResult_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_GetResult_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "connect4_msgs/action/detail/deliver_block__functions.h"

bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__init(connect4_msgs__action__DeliverBlock_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!connect4_msgs__action__DeliverBlock_Feedback__init(&msg->feedback)) {
    connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(connect4_msgs__action__DeliverBlock_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  connect4_msgs__action__DeliverBlock_Feedback__fini(&msg->feedback);
}

bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__are_equal(const connect4_msgs__action__DeliverBlock_FeedbackMessage * lhs, const connect4_msgs__action__DeliverBlock_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!connect4_msgs__action__DeliverBlock_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__copy(
  const connect4_msgs__action__DeliverBlock_FeedbackMessage * input,
  connect4_msgs__action__DeliverBlock_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!connect4_msgs__action__DeliverBlock_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

connect4_msgs__action__DeliverBlock_FeedbackMessage *
connect4_msgs__action__DeliverBlock_FeedbackMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_FeedbackMessage * msg = (connect4_msgs__action__DeliverBlock_FeedbackMessage *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__action__DeliverBlock_FeedbackMessage));
  bool success = connect4_msgs__action__DeliverBlock_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__action__DeliverBlock_FeedbackMessage__destroy(connect4_msgs__action__DeliverBlock_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__init(connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_FeedbackMessage * data = NULL;

  if (size) {
    data = (connect4_msgs__action__DeliverBlock_FeedbackMessage *)allocator.zero_allocate(size, sizeof(connect4_msgs__action__DeliverBlock_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__action__DeliverBlock_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__fini(connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence *
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * array = (connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence *)allocator.allocate(sizeof(connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__destroy(connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__are_equal(const connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * lhs, const connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__copy(
  const connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * input,
  connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__action__DeliverBlock_FeedbackMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__action__DeliverBlock_FeedbackMessage * data =
      (connect4_msgs__action__DeliverBlock_FeedbackMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__action__DeliverBlock_FeedbackMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__action__DeliverBlock_FeedbackMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__action__DeliverBlock_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
