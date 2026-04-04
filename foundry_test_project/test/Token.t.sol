// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Test} from "forge-std/Test.sol";
import {Token} from "../src/Token.sol";

contract TokenTest is Test {
    Token public token;
    
    function setUp() public {
        token = new Token();
    }

    function test_owner() public view {
        assertEq(token.owner(), address(this));
    }

    function test_mint() public {
        token.mint(address(this), 100);
        assertEq(token.balanceOf(address(this)), 100);
    }

    function test_transfer() public {
        token.mint(address(this), 100);
        token.transfer(address(0x1), 20);
        assertEq(token.balanceOf(address(this)), 80);
        assertEq(token.balanceOf(address(0x1)), 20);
    }

    function test_transfer_insufficient() public {
        vm.expectRevert("Insufficient balance");
        token.transfer(address(0x1), 100);
    }

    function test_mint_only_owner() public {
        vm.expectRevert("Only owner can mint");
        vm.prank(address(0x1));
        token.mint(address(0x1), 100);
    }

    function testFuzz_transfer(uint256 x) public {
        vm.assume(x <= 10000);
        token.mint(address(this), 10000);
        token.transfer(address(0x1), x);
        uint256 total_amount = token.balanceOf(address(this)) + token.balanceOf(address(0x1));
        assertEq(total_amount, 10000);
    }

}





