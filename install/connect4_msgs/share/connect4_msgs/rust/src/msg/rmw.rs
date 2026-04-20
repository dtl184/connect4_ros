#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__msg__BoardState() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__msg__BoardState__init(msg: *mut BoardState) -> bool;
    fn connect4_msgs__msg__BoardState__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<BoardState>, size: usize) -> bool;
    fn connect4_msgs__msg__BoardState__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<BoardState>);
    fn connect4_msgs__msg__BoardState__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<BoardState>, out_seq: *mut rosidl_runtime_rs::Sequence<BoardState>) -> bool;
}

// Corresponds to connect4_msgs__msg__BoardState
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BoardState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub cells: rosidl_runtime_rs::Sequence<i32>,

}



impl Default for BoardState {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__msg__BoardState__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__msg__BoardState__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for BoardState {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__BoardState__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__BoardState__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__BoardState__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for BoardState {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for BoardState where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/msg/BoardState";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__msg__BoardState() }
  }
}


#[link(name = "connect4_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__msg__Winner() -> *const std::ffi::c_void;
}

#[link(name = "connect4_msgs__rosidl_generator_c")]
extern "C" {
    fn connect4_msgs__msg__Winner__init(msg: *mut Winner) -> bool;
    fn connect4_msgs__msg__Winner__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Winner>, size: usize) -> bool;
    fn connect4_msgs__msg__Winner__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Winner>);
    fn connect4_msgs__msg__Winner__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Winner>, out_seq: *mut rosidl_runtime_rs::Sequence<Winner>) -> bool;
}

// Corresponds to connect4_msgs__msg__Winner
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Winner {

    // This member is not documented.
    #[allow(missing_docs)]
    pub winner: i32,

}



impl Default for Winner {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !connect4_msgs__msg__Winner__init(&mut msg as *mut _) {
        panic!("Call to connect4_msgs__msg__Winner__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Winner {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__Winner__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__Winner__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { connect4_msgs__msg__Winner__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Winner {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Winner where Self: Sized {
  const TYPE_NAME: &'static str = "connect4_msgs/msg/Winner";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__connect4_msgs__msg__Winner() }
  }
}


