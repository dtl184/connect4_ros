// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "connect4_msgs/msg/winner.hpp"


#ifndef CONNECT4_MSGS__MSG__DETAIL__WINNER__TRAITS_HPP_
#define CONNECT4_MSGS__MSG__DETAIL__WINNER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "connect4_msgs/msg/detail/winner__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace connect4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Winner & msg,
  std::ostream & out)
{
  out << "{";
  // member: winner
  {
    out << "winner: ";
    rosidl_generator_traits::value_to_yaml(msg.winner, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Winner & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: winner
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "winner: ";
    rosidl_generator_traits::value_to_yaml(msg.winner, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Winner & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace connect4_msgs

namespace rosidl_generator_traits
{

[[deprecated("use connect4_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const connect4_msgs::msg::Winner & msg,
  std::ostream & out, size_t indentation = 0)
{
  connect4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use connect4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const connect4_msgs::msg::Winner & msg)
{
  return connect4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<connect4_msgs::msg::Winner>()
{
  return "connect4_msgs::msg::Winner";
}

template<>
inline const char * name<connect4_msgs::msg::Winner>()
{
  return "connect4_msgs/msg/Winner";
}

template<>
struct has_fixed_size<connect4_msgs::msg::Winner>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<connect4_msgs::msg::Winner>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<connect4_msgs::msg::Winner>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CONNECT4_MSGS__MSG__DETAIL__WINNER__TRAITS_HPP_
