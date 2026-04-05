// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from connect4_msgs:msg/Winner.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "connect4_msgs/msg/detail/winner__struct.h"
#include "connect4_msgs/msg/detail/winner__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool connect4_msgs__msg__winner__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
    if (class_attr == NULL) {
      return false;
    }
    PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
    if (name_attr == NULL) {
      Py_DECREF(class_attr);
      return false;
    }
    PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
    if (module_attr == NULL) {
      Py_DECREF(name_attr);
      Py_DECREF(class_attr);
      return false;
    }

    // PyUnicode_1BYTE_DATA is just a cast
    assert(strncmp("connect4_msgs.msg._winner", (char *)PyUnicode_1BYTE_DATA(module_attr), 25) == 0);
    assert(strncmp("Winner", (char *)PyUnicode_1BYTE_DATA(name_attr), 6) == 0);

    Py_DECREF(module_attr);
    Py_DECREF(name_attr);
    Py_DECREF(class_attr);
  }
  connect4_msgs__msg__Winner * ros_message = _ros_message;
  {  // winner
    PyObject * field = PyObject_GetAttrString(_pymsg, "winner");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->winner = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * connect4_msgs__msg__winner__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Winner */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("connect4_msgs.msg._winner");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Winner");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  connect4_msgs__msg__Winner * ros_message = (connect4_msgs__msg__Winner *)raw_ros_message;
  {  // winner
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->winner);
    {
      int rc = PyObject_SetAttrString(_pymessage, "winner", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
