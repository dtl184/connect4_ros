// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "connect4_msgs/msg/winner.hpp"


#ifndef CONNECT4_MSGS__MSG__DETAIL__WINNER__BUILDER_HPP_
#define CONNECT4_MSGS__MSG__DETAIL__WINNER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "connect4_msgs/msg/detail/winner__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace connect4_msgs
{

namespace msg
{

namespace builder
{

class Init_Winner_winner
{
public:
  Init_Winner_winner()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::connect4_msgs::msg::Winner winner(::connect4_msgs::msg::Winner::_winner_type arg)
  {
    msg_.winner = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::msg::Winner msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::msg::Winner>()
{
  return connect4_msgs::msg::builder::Init_Winner_winner();
}

}  // namespace connect4_msgs

#endif  // CONNECT4_MSGS__MSG__DETAIL__WINNER__BUILDER_HPP_
