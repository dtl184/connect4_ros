
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Goal() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_Goal__init(msg: *mut DeliverBlock_Goal) -> bool;
    fn connect4_msgs__action__DeliverBlock_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Goal>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Goal>);
    fn connect4_msgs__action__DeliverBlock_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Goal>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub player: i32,

}



impl Default for DeliverBlock_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_Goal__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Goal() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Result() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_Result__init(msg: *mut DeliverBlock_Result) -> bool;
    fn connect4_msgs__action__DeliverBlock_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Result>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Result>);
    fn connect4_msgs__action__DeliverBlock_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Result>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: rosidl_runtime_rs::String,

}



impl Default for DeliverBlock_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_Result__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_Result where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Result() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_Feedback__init(msg: *mut DeliverBlock_Feedback) -> bool;
    fn connect4_msgs__action__DeliverBlock_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Feedback>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Feedback>);
    fn connect4_msgs__action__DeliverBlock_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_Feedback>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: rosidl_runtime_rs::String,

}



impl Default for DeliverBlock_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_Feedback__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_Feedback() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_FeedbackMessage__init(msg: *mut DeliverBlock_FeedbackMessage) -> bool;
    fn connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_FeedbackMessage>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_FeedbackMessage>);
    fn connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_FeedbackMessage>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::DeliverBlock_Feedback,

}



impl Default for DeliverBlock_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_FeedbackMessage() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Goal() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_Goal__init(msg: *mut ResetBoard_Goal) -> bool;
    fn connect4_msgs__action__ResetBoard_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Goal>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Goal>);
    fn connect4_msgs__action__ResetBoard_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Goal>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub final_board_state: super::super::msg::rmw::BoardState,

}



impl Default for ResetBoard_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_Goal__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Goal() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Result() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_Result__init(msg: *mut ResetBoard_Result) -> bool;
    fn connect4_msgs__action__ResetBoard_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Result>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Result>);
    fn connect4_msgs__action__ResetBoard_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Result>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: rosidl_runtime_rs::String,

}



impl Default for ResetBoard_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_Result__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_Result where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Result() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_Feedback__init(msg: *mut ResetBoard_Feedback) -> bool;
    fn connect4_msgs__action__ResetBoard_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Feedback>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Feedback>);
    fn connect4_msgs__action__ResetBoard_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_Feedback>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: rosidl_runtime_rs::String,

}



impl Default for ResetBoard_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_Feedback__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_Feedback() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_FeedbackMessage__init(msg: *mut ResetBoard_FeedbackMessage) -> bool;
    fn connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_FeedbackMessage>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_FeedbackMessage>);
    fn connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_FeedbackMessage>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::ResetBoard_Feedback,

}



impl Default for ResetBoard_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_FeedbackMessage() }
  }
}




#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_SendGoal_Request__init(msg: *mut DeliverBlock_SendGoal_Request) -> bool;
    fn connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Request>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Request>);
    fn connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Request>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::DeliverBlock_Goal,

}



impl Default for DeliverBlock_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal_Request() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_SendGoal_Response__init(msg: *mut DeliverBlock_SendGoal_Response) -> bool;
    fn connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Response>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Response>);
    fn connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_SendGoal_Response>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for DeliverBlock_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal_Response() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_GetResult_Request__init(msg: *mut DeliverBlock_GetResult_Request) -> bool;
    fn connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Request>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Request>);
    fn connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Request>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for DeliverBlock_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult_Request() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__DeliverBlock_GetResult_Response__init(msg: *mut DeliverBlock_GetResult_Response) -> bool;
    fn connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Response>, size: usize) -> bool;
    fn connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Response>);
    fn connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DeliverBlock_GetResult_Response>) -> bool;
}

// Corresponds to connect4_msgs__action__DeliverBlock_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DeliverBlock_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::DeliverBlock_Result,

}



impl Default for DeliverBlock_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__DeliverBlock_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__DeliverBlock_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DeliverBlock_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__DeliverBlock_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DeliverBlock_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DeliverBlock_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/DeliverBlock_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult_Response() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_SendGoal_Request__init(msg: *mut ResetBoard_SendGoal_Request) -> bool;
    fn connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Request>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Request>);
    fn connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Request>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::ResetBoard_Goal,

}



impl Default for ResetBoard_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal_Request() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_SendGoal_Response__init(msg: *mut ResetBoard_SendGoal_Response) -> bool;
    fn connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Response>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Response>);
    fn connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_SendGoal_Response>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for ResetBoard_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal_Response() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_GetResult_Request__init(msg: *mut ResetBoard_GetResult_Request) -> bool;
    fn connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Request>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Request>);
    fn connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Request>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for ResetBoard_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_GetResult_Request() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__action__ResetBoard_GetResult_Response__init(msg: *mut ResetBoard_GetResult_Response) -> bool;
    fn connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Response>, size: usize) -> bool;
    fn connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Response>);
    fn connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetBoard_GetResult_Response>) -> bool;
}

// Corresponds to connect4_msgs__action__ResetBoard_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetBoard_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::ResetBoard_Result,

}



impl Default for ResetBoard_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__action__ResetBoard_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__action__ResetBoard_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetBoard_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__action__ResetBoard_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetBoard_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetBoard_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/action/ResetBoard_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__action__ResetBoard_GetResult_Response() }
  }
}






#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to connect4_msgs__action__DeliverBlock_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct DeliverBlock_SendGoal;

impl rosidl_runtime_rs::Service for DeliverBlock_SendGoal {
    type Request = DeliverBlock_SendGoal_Request;
    type Response = DeliverBlock_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__DeliverBlock_SendGoal() }
    }
}




#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to connect4_msgs__action__DeliverBlock_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct DeliverBlock_GetResult;

impl rosidl_runtime_rs::Service for DeliverBlock_GetResult {
    type Request = DeliverBlock_GetResult_Request;
    type Response = DeliverBlock_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__DeliverBlock_GetResult() }
    }
}




#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to connect4_msgs__action__ResetBoard_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct ResetBoard_SendGoal;

impl rosidl_runtime_rs::Service for ResetBoard_SendGoal {
    type Request = ResetBoard_SendGoal_Request;
    type Response = ResetBoard_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__ResetBoard_SendGoal() }
    }
}




#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__ResetBoard_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to connect4_msgs__action__ResetBoard_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct ResetBoard_GetResult;

impl rosidl_runtime_rs::Service for ResetBoard_GetResult {
    type Request = ResetBoard_GetResult_Request;
    type Response = ResetBoard_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__connect4_msgs__action__ResetBoard_GetResult() }
    }
}


