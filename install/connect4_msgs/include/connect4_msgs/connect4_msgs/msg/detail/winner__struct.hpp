// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice

#ifndef CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_HPP_
#define CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__connect4_msgs__msg__Winner __attribute__((deprecated))
#else
# define DEPRECATED__connect4_msgs__msg__Winner __declspec(deprecated)
#endif

namespace connect4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Winner_
{
  using Type = Winner_<ContainerAllocator>;

  explicit Winner_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->winner = 0l;
    }
  }

  explicit Winner_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->winner = 0l;
    }
  }

  // field types and members
  using _winner_type =
    int32_t;
  _winner_type winner;

  // setters for named parameter idiom
  Type & set__winner(
    const int32_t & _arg)
  {
    this->winner = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    connect4_msgs::msg::Winner_<ContainerAllocator> *;
  using ConstRawPtr =
    const connect4_msgs::msg::Winner_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<connect4_msgs::msg::Winner_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<connect4_msgs::msg::Winner_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      connect4_msgs::msg::Winner_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<connect4_msgs::msg::Winner_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      connect4_msgs::msg::Winner_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<connect4_msgs::msg::Winner_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<connect4_msgs::msg::Winner_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<connect4_msgs::msg::Winner_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__connect4_msgs__msg__Winner
    std::shared_ptr<connect4_msgs::msg::Winner_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__connect4_msgs__msg__Winner
    std::shared_ptr<connect4_msgs::msg::Winner_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Winner_ & other) const
  {
    if (this->winner != other.winner) {
      return false;
    }
    return true;
  }
  bool operator!=(const Winner_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Winner_

// alias to use template instance with default allocator
using Winner =
  connect4_msgs::msg::Winner_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace connect4_msgs

#endif  // CONNECT4_MSGS__MSG__DETAIL__WINNER__STRUCT_HPP_
