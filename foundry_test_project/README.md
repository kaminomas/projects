# foundry_test_project 🟢

Smart-contract tests written in **native Solidity** with [Foundry](https://book.getfoundry.sh/) (`forge`). Pairs with `hardhat_test_project/` — the same contracts are also covered there via JavaScript (Mocha / Chai) tests. The goal is to show both toolchains and contrast their testing idioms.

## Stack

- **Solidity** (contracts: `Token`, `Counter`)
- **Foundry** (`forge test`, `anvil`, `cast`)
- Tests are themselves Solidity (`*.t.sol`) — no JS bridge

## What's interesting here

- **Fuzz testing** via `forge test`'s built-in property-based fuzzer (e.g. transfer invariants over arbitrary amounts).
- **Cheatcodes**: `vm.prank` to switch the `msg.sender`, `vm.expectRevert` to assert failure paths precisely, `vm.assume` to constrain fuzz inputs without sacrificing coverage.
- **No JS glue** — tests, assertions, and setup all live in Solidity, which means less context-switching when reasoning about contract behavior.

## Layout

```
foundry_test_project/
├── src/
│   ├── Counter.sol
│   └── Token.sol
├── test/
│   ├── Counter.t.sol
│   └── Token.t.sol
├── script/                   # forge script deploys
├── foundry.toml
└── lib/                      # forge-std (gitignored)
```

## Run

```bash
cd foundry_test_project
forge install                 # pulls forge-std into lib/
forge build
forge test -vv                # -vvv / -vvvv for deeper traces

# Gas snapshot
forge snapshot

# Local node (separate terminal)
anvil

# Deploy example
forge script script/Counter.s.sol:CounterScript \
  --rpc-url <your_rpc_url> --private-key <your_private_key>
```

## Why both Hardhat and Foundry?

Real teams tend to pick one, but being fluent in both matters:

- **Hardhat / ethers.js** — familiar JS/TS ergonomics, rich plugin ecosystem, easy to integrate with frontends.
- **Foundry** — orders-of-magnitude faster, Solidity-native tests, first-class fuzzing and invariant testing.

Having both side-by-side makes the trade-offs concrete instead of theoretical.
