// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice
#include "connect4_msgs/msg/detail/board_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `cells`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
connect4_msgs__msg__BoardState__init(connect4_msgs__msg__BoardState * msg)
{
  if (!msg) {
    return false;
  }
  // cells
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->cells, 0)) {
    connect4_msgs__msg__BoardState__fini(msg);
    return false;
  }
  return true;
}

void
connect4_msgs__msg__BoardState__fini(connect4_msgs__msg__BoardState * msg)
{
  if (!msg) {
    return;
  }
  // cells
  rosidl_runtime_c__int32__Sequence__fini(&msg->cells);
}

bool
connect4_msgs__msg__BoardState__are_equal(const connect4_msgs__msg__BoardState * lhs, const connect4_msgs__msg__BoardState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // cells
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->cells), &(rhs->cells)))
  {
    return false;
  }
  return true;
}

bool
connect4_msgs__msg__BoardState__copy(
  const connect4_msgs__msg__BoardState * input,
  connect4_msgs__msg__BoardState * output)
{
  if (!input || !output) {
    return false;
  }
  // cells
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->cells), &(output->cells)))
  {
    return false;
  }
  return true;
}

connect4_msgs__msg__BoardState *
connect4_msgs__msg__BoardState__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__BoardState * msg = (connect4_msgs__msg__BoardState *)allocator.allocate(sizeof(connect4_msgs__msg__BoardState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__msg__BoardState));
  bool success = connect4_msgs__msg__BoardState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__msg__BoardState__destroy(connect4_msgs__msg__BoardState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__msg__BoardState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__msg__BoardState__Sequence__init(connect4_msgs__msg__BoardState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__BoardState * data = NULL;

  if (size) {
    data = (connect4_msgs__msg__BoardState *)allocator.zero_allocate(size, sizeof(connect4_msgs__msg__BoardState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__msg__BoardState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__msg__BoardState__fini(&data[i - 1]);
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
connect4_msgs__msg__BoardState__Sequence__fini(connect4_msgs__msg__BoardState__Sequence * array)
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
      connect4_msgs__msg__BoardState__fini(&array->data[i]);
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

connect4_msgs__msg__BoardState__Sequence *
connect4_msgs__msg__BoardState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__BoardState__Sequence * array = (connect4_msgs__msg__BoardState__Sequence *)allocator.allocate(sizeof(connect4_msgs__msg__BoardState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__msg__BoardState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__msg__BoardState__Sequence__destroy(connect4_msgs__msg__BoardState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__msg__BoardState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__msg__BoardState__Sequence__are_equal(const connect4_msgs__msg__BoardState__Sequence * lhs, const connect4_msgs__msg__BoardState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__msg__BoardState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__msg__BoardState__Sequence__copy(
  const connect4_msgs__msg__BoardState__Sequence * input,
  connect4_msgs__msg__BoardState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__msg__BoardState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__msg__BoardState * data =
      (connect4_msgs__msg__BoardState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__msg__BoardState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__msg__BoardState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__msg__BoardState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
