#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to connect4_msgs__msg__BoardState

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BoardState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub cells: Vec<i32>,

}



impl Default for BoardState {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::BoardState::default())
  }
}

impl rosidl_runtime_rs::Message for BoardState {
  type RmwMsg = super::msg::rmw::BoardState;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        cells: msg.cells.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        cells: msg.cells.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      cells: msg.cells
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to connect4_msgs__msg__Winner

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Winner {

    // This member is not documented.
    #[allow(missing_docs)]
    pub winner: i32,

}



impl Default for Winner {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Winner::default())
  }
}

impl rosidl_runtime_rs::Message for Winner {
  type RmwMsg = super::msg::rmw::Winner;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        winner: msg.winner,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      winner: msg.winner,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      winner: msg.winner,
    }
  }
}


