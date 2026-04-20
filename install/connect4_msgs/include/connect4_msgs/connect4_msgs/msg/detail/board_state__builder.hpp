// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from connect4_msgs:msg/BoardState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "connect4_msgs/msg/board_state.hpp"


#ifndef CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__BUILDER_HPP_
#define CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "connect4_msgs/msg/detail/board_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace connect4_msgs
{

namespace msg
{

namespace builder
{

class Init_BoardState_cells
{
public:
  Init_BoardState_cells()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::connect4_msgs::msg::BoardState cells(::connect4_msgs::msg::BoardState::_cells_type arg)
  {
    msg_.cells = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::msg::BoardState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::msg::BoardState>()
{
  return connect4_msgs::msg::builder::Init_BoardState_cells();
}

}  // namespace connect4_msgs

#endif  // CONNECT4_MSGS__MSG__DETAIL__BOARD_STATE__BUILDER_HPP_
