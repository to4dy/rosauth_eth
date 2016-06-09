cmake_minimum_required(VERSION 2.8.3)
project(rosauth)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  rostest
)

catkin_python_setup()
add_service_files(
  FILES
  Authentication.srv
)
generate_messages(
  DEPENDENCIES
  std_msgs
)
catkin_package(
CATKIN_DEPENDS roscpp message_runtime
)

catkin_install_python(PROGRAMS nodes/authentication.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)



install(DIRECTORY launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if(CATKIN_ENABLE_TESTING)
  ## Add gtest based cpp test target and link libraries
  add_executable(ros_mac_authentication_test test/ros_mac_authentication_test.cpp)
  add_dependencies(ros_mac_authentication_test ${PROJECT_NAME}_gencpp)
  target_link_libraries(ros_mac_authentication_test ${catkin_LIBRARIES} ${GTEST_LIBRARIES} crypto dl pthread)
endif()
