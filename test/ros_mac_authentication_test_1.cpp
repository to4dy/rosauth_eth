#include <fstream>
#include <gtest/gtest.h>
#include <openssl/sha.h>
#include <ros/ros.h>
#include <rosauth/Authentication.h>
#include <sstream>
#include <string>

using namespace std;
using namespace ros;

ServiceClient client;

TEST(RosHashAuthentication, validAuthentication)
{
  string msg = "bc8c629cd7477fd580b8f9e8da49e5aad364b769192.168.1.101192.168.1.1111337";
  string sign = "5a436753ef5b30b77951707b893c65343129c51d79d0a67bb746830ee7d6412bfd730c46b5b9be3a4651f542a163c7b7a38b711bea6e16f3cc4bc478c382f301";
  string addr = "a28779d29c49fd57d0fc4130e5ebec07c2c79ef5";

    // make the request
  rosauth::Authentication srv;
  srv.request.msg = msg;
  srv.request.sign = sign;
  srv.request.addr = addr;


  EXPECT_TRUE(client.call(srv));
  EXPECT_TRUE(srv.response.authenticated);

  string msg1 = "bc8c629cd7477fd580b8f9e8da49e5aad364b769192.168.1.101192.168.1.1111337";
  string sign1 = "ff436753ef5b30b77951707b893c65343129c51d79d0a67bb746830ee7d6412bfd730c46b5b9be3a4651f542a163c7b7a38b711bea6e16f3cc4bc478c382f301";
  string addr1 = "a28779d29c49fd57d0fc4130e5ebec07c2c79ef5";

    // make the request
  rosauth::Authentication srv1;
  srv1.request.msg = msg1;
  srv1.request.sign = sign1;
  srv1.request.addr = addr1;


  EXPECT_TRUE(client.call(srv1));
  EXPECT_FALSE(srv1.response.authenticated);


}

// Run all the tests that were declared with TEST()
int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);

  // initialize ROS and the node
  init(argc, argv, "ros_hash_authentication_test");
  NodeHandle node;

  // setup the service client
  client = node.serviceClient<rosauth::Authentication>("authenticate");

  return RUN_ALL_TESTS();
}
