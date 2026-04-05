// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice
#include "connect4_msgs/msg/detail/winner__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
connect4_msgs__msg__Winner__init(connect4_msgs__msg__Winner * msg)
{
  if (!msg) {
    return false;
  }
  // winner
  return true;
}

void
connect4_msgs__msg__Winner__fini(connect4_msgs__msg__Winner * msg)
{
  if (!msg) {
    return;
  }
  // winner
}

bool
connect4_msgs__msg__Winner__are_equal(const connect4_msgs__msg__Winner * lhs, const connect4_msgs__msg__Winner * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // winner
  if (lhs->winner != rhs->winner) {
    return false;
  }
  return true;
}

bool
connect4_msgs__msg__Winner__copy(
  const connect4_msgs__msg__Winner * input,
  connect4_msgs__msg__Winner * output)
{
  if (!input || !output) {
    return false;
  }
  // winner
  output->winner = input->winner;
  return true;
}

connect4_msgs__msg__Winner *
connect4_msgs__msg__Winner__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__Winner * msg = (connect4_msgs__msg__Winner *)allocator.allocate(sizeof(connect4_msgs__msg__Winner), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(connect4_msgs__msg__Winner));
  bool success = connect4_msgs__msg__Winner__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
connect4_msgs__msg__Winner__destroy(connect4_msgs__msg__Winner * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    connect4_msgs__msg__Winner__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
connect4_msgs__msg__Winner__Sequence__init(connect4_msgs__msg__Winner__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__Winner * data = NULL;

  if (size) {
    data = (connect4_msgs__msg__Winner *)allocator.zero_allocate(size, sizeof(connect4_msgs__msg__Winner), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = connect4_msgs__msg__Winner__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        connect4_msgs__msg__Winner__fini(&data[i - 1]);
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
connect4_msgs__msg__Winner__Sequence__fini(connect4_msgs__msg__Winner__Sequence * array)
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
      connect4_msgs__msg__Winner__fini(&array->data[i]);
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

connect4_msgs__msg__Winner__Sequence *
connect4_msgs__msg__Winner__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  connect4_msgs__msg__Winner__Sequence * array = (connect4_msgs__msg__Winner__Sequence *)allocator.allocate(sizeof(connect4_msgs__msg__Winner__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = connect4_msgs__msg__Winner__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
connect4_msgs__msg__Winner__Sequence__destroy(connect4_msgs__msg__Winner__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    connect4_msgs__msg__Winner__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
connect4_msgs__msg__Winner__Sequence__are_equal(const connect4_msgs__msg__Winner__Sequence * lhs, const connect4_msgs__msg__Winner__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!connect4_msgs__msg__Winner__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
connect4_msgs__msg__Winner__Sequence__copy(
  const connect4_msgs__msg__Winner__Sequence * input,
  connect4_msgs__msg__Winner__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(connect4_msgs__msg__Winner);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    connect4_msgs__msg__Winner * data =
      (connect4_msgs__msg__Winner *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!connect4_msgs__msg__Winner__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          connect4_msgs__msg__Winner__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!connect4_msgs__msg__Winner__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
