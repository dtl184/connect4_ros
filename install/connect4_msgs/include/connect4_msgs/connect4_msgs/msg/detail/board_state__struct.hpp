// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice

#ifndef CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__STRUCT_HPP_
#define CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__connect4_msgs__msg__BoardState __attribute__((deprecated))
#else
# define DEPRECATED__connect4_msgs__msg__BoardState __declspec(deprecated)
#endif

namespace connect4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BoardState_
{
  using Type = BoardState_<ContainerAllocator>;

  explicit BoardState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit BoardState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _cells_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _cells_type cells;

  // setters for named parameter idiom
  Type & set__cells(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->cells = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    connect4_msgs::msg::BoardState_<ContainerAllocator> *;
  using ConstRawPtr =
    const connect4_msgs::msg::BoardState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      connect4_msgs::msg::BoardState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      connect4_msgs::msg::BoardState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__connect4_msgs__msg__BoardState
    std::shared_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__connect4_msgs__msg__BoardState
    std::shared_ptr<connect4_msgs::msg::BoardState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BoardState_ & other) const
  {
    if (this->cells != other.cells) {
      return false;
    }
    return true;
  }
  bool operator!=(const BoardState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BoardState_

// alias to use template instance with default allocator
using BoardState =
  connect4_msgs::msg::BoardState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace connect4_msgs

#endif  // CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__STRUCT_HPP_
