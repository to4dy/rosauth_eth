#!/usr/bin/env python
import bitcoin
from ethereum import utils
import rospy
from std_msgs.msg import String
from rosauth.srv import *
from web3 import Web3, RPCProvider, IPCProvider

def check_signature(req):
    signature = "0x" + req.sign
    contract = "0x" + req.contract
    client = req.client
    dest = req.dest
    rand = req.rand
    t = req.t.secs
    end = req.end.secs

    msg = contract + client + dest + rand + str(t) + str(end)


    
    web3 = Web3(RPCProvider(host="127.0.0.1", port="8545"))
    web3.config.defaultAccount = '0xa28779d29c49fd57d0fc4130e5ebec07c2c79ef5'
    abi = '[{"constant":false,"inputs":[],"name":"kill","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"owns","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"type":"constructor"}]'
    contracto= web3.eth.contract(abi)
    inst=contracto.at('0xbc8c629cd7477fd580b8f9e8da49e5aad364b769')


    if (int(t) > int(rospy.get_rostime().secs)):
        diff = t - int(rospy.get_rostime().secs)
    else:
        diff = int(rospy.get_rostime().secs) - t
    if (diff > 600):
        return False


    print "msg: " + msg + " sign: " + signature + " contract: " + contract

    hash_msg = utils.sha3(msg).encode('hex')
    r = long(signature[0:66], 16)
    s = long('0x' + signature[66:130], 16)
    v = long('0x' + signature[130:132], 16)
    if not (v == 27 and v == 28):
        v += 27
    address_from_hash = bitcoin.ecdsa_raw_recover(
        hash_msg.decode('hex'), (v, r, s))
    public_key = bitcoin.encode_pubkey(address_from_hash, 'bin')

    if ('0x' + utils.sha3(public_key[1:]).encode('hex')[24:64] == inst.owns()):
        return True
    else:
        return False
     

    
s = rospy.Service('authenticate', Authentication, check_signature)


def main():
    
        rospy.init_node('authenticate', anonymous=False)
        rospy.spin()
  

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


