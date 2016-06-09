Dummy contract: 0xbc8c629cd7477fd580b8f9e8da49e5aad364b769


fuction owns 0xcec1b7100000000000000000000000000000000000000000000000000000000000000005

curl localhost:8545 -X POST --data '{"jsonrpc":"2.0", "method":"eth_call", "params":[{"from": "eth.accounts[0]", "to": "0xbc8c629cd7477fd580b8f9e8da49e5aad364b769", "data": "0xcec1b7100000000000000000000000000000000000000000000000000000000000000005"}], "id":1}'
/*
	Contract code
*/

contract mortal {
    /* Define variable owner of the type address*/
    address owner;
    
    function owns() constant returns (address) {
        return owner;
    }

    /* this function is executed at initialization and sets the owner of the contract */
    function mortal() { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() { if (msg.sender == owner) suicide(owner); }
    
}

contract greeter is mortal {
    /* define variable greeting of the type string */
    string greeting;

    /* this runs when the contract is executed */
    function greeter(string _greeting) public {
        greeting = _greeting;
    }

    /* main function */
    function greet() constant returns (string) {
        return greeting;
    }
}

/*
*
* ABI
*
*/

[{"constant":false,"inputs":[],"name":"kill","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"owns","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"type":"constructor"}]

