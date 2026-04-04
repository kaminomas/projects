// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Token {
    mapping(address => uint256) public balanceOf;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function mint(address to, uint256 amount) public {
        require(msg.sender == owner, "Only owner can mint");
        balanceOf[to] += amount;
    }

    function transfer(address to, uint256 amount) public {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
    }
}
