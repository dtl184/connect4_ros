// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from connect4_msgs:action/ResetBoard.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "connect4_msgs/action/reset_board.hpp"


#ifndef CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__BUILDER_HPP_
#define CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "connect4_msgs/action/detail/reset_board__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_Goal_final_board_state
{
public:
  Init_ResetBoard_Goal_final_board_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::connect4_msgs::action::ResetBoard_Goal final_board_state(::connect4_msgs::action::ResetBoard_Goal::_final_board_state_type arg)
  {
    msg_.final_board_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_Goal>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_Goal_final_board_state();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_Result_message
{
public:
  explicit Init_ResetBoard_Result_message(::connect4_msgs::action::ResetBoard_Result & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_Result message(::connect4_msgs::action::ResetBoard_Result::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_Result msg_;
};

class Init_ResetBoard_Result_success
{
public:
  Init_ResetBoard_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_Result_message success(::connect4_msgs::action::ResetBoard_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ResetBoard_Result_message(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_Result>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_Result_success();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_Feedback_status
{
public:
  Init_ResetBoard_Feedback_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::connect4_msgs::action::ResetBoard_Feedback status(::connect4_msgs::action::ResetBoard_Feedback::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_Feedback>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_Feedback_status();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_SendGoal_Request_goal
{
public:
  explicit Init_ResetBoard_SendGoal_Request_goal(::connect4_msgs::action::ResetBoard_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_SendGoal_Request goal(::connect4_msgs::action::ResetBoard_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Request msg_;
};

class Init_ResetBoard_SendGoal_Request_goal_id
{
public:
  Init_ResetBoard_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_SendGoal_Request_goal goal_id(::connect4_msgs::action::ResetBoard_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_ResetBoard_SendGoal_Request_goal(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_SendGoal_Request>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_SendGoal_Request_goal_id();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_SendGoal_Response_stamp
{
public:
  explicit Init_ResetBoard_SendGoal_Response_stamp(::connect4_msgs::action::ResetBoard_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_SendGoal_Response stamp(::connect4_msgs::action::ResetBoard_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Response msg_;
};

class Init_ResetBoard_SendGoal_Response_accepted
{
public:
  Init_ResetBoard_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_SendGoal_Response_stamp accepted(::connect4_msgs::action::ResetBoard_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_ResetBoard_SendGoal_Response_stamp(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_SendGoal_Response>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_SendGoal_Response_accepted();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_SendGoal_Event_response
{
public:
  explicit Init_ResetBoard_SendGoal_Event_response(::connect4_msgs::action::ResetBoard_SendGoal_Event & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_SendGoal_Event response(::connect4_msgs::action::ResetBoard_SendGoal_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Event msg_;
};

class Init_ResetBoard_SendGoal_Event_request
{
public:
  explicit Init_ResetBoard_SendGoal_Event_request(::connect4_msgs::action::ResetBoard_SendGoal_Event & msg)
  : msg_(msg)
  {}
  Init_ResetBoard_SendGoal_Event_response request(::connect4_msgs::action::ResetBoard_SendGoal_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ResetBoard_SendGoal_Event_response(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Event msg_;
};

class Init_ResetBoard_SendGoal_Event_info
{
public:
  Init_ResetBoard_SendGoal_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_SendGoal_Event_request info(::connect4_msgs::action::ResetBoard_SendGoal_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ResetBoard_SendGoal_Event_request(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_SendGoal_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_SendGoal_Event>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_SendGoal_Event_info();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_GetResult_Request_goal_id
{
public:
  Init_ResetBoard_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::connect4_msgs::action::ResetBoard_GetResult_Request goal_id(::connect4_msgs::action::ResetBoard_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_GetResult_Request>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_GetResult_Request_goal_id();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_GetResult_Response_result
{
public:
  explicit Init_ResetBoard_GetResult_Response_result(::connect4_msgs::action::ResetBoard_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_GetResult_Response result(::connect4_msgs::action::ResetBoard_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Response msg_;
};

class Init_ResetBoard_GetResult_Response_status
{
public:
  Init_ResetBoard_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_GetResult_Response_result status(::connect4_msgs::action::ResetBoard_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_ResetBoard_GetResult_Response_result(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_GetResult_Response>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_GetResult_Response_status();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_GetResult_Event_response
{
public:
  explicit Init_ResetBoard_GetResult_Event_response(::connect4_msgs::action::ResetBoard_GetResult_Event & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_GetResult_Event response(::connect4_msgs::action::ResetBoard_GetResult_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Event msg_;
};

class Init_ResetBoard_GetResult_Event_request
{
public:
  explicit Init_ResetBoard_GetResult_Event_request(::connect4_msgs::action::ResetBoard_GetResult_Event & msg)
  : msg_(msg)
  {}
  Init_ResetBoard_GetResult_Event_response request(::connect4_msgs::action::ResetBoard_GetResult_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ResetBoard_GetResult_Event_response(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Event msg_;
};

class Init_ResetBoard_GetResult_Event_info
{
public:
  Init_ResetBoard_GetResult_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_GetResult_Event_request info(::connect4_msgs::action::ResetBoard_GetResult_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ResetBoard_GetResult_Event_request(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_GetResult_Event msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_GetResult_Event>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_GetResult_Event_info();
}

}  // namespace connect4_msgs


namespace connect4_msgs
{

namespace action
{

namespace builder
{

class Init_ResetBoard_FeedbackMessage_feedback
{
public:
  explicit Init_ResetBoard_FeedbackMessage_feedback(::connect4_msgs::action::ResetBoard_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::connect4_msgs::action::ResetBoard_FeedbackMessage feedback(::connect4_msgs::action::ResetBoard_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_FeedbackMessage msg_;
};

class Init_ResetBoard_FeedbackMessage_goal_id
{
public:
  Init_ResetBoard_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetBoard_FeedbackMessage_feedback goal_id(::connect4_msgs::action::ResetBoard_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_ResetBoard_FeedbackMessage_feedback(msg_);
  }

private:
  ::connect4_msgs::action::ResetBoard_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::connect4_msgs::action::ResetBoard_FeedbackMessage>()
{
  return connect4_msgs::action::builder::Init_ResetBoard_FeedbackMessage_goal_id();
}

}  // namespace connect4_msgs

#endif  // CONNECT4_MSGS__ACTION__DETAIL__RESET_BOARD__BUILDER_HPP_
