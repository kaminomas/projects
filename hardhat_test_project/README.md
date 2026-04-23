# hardhat_test_project 🟢

Smart-contract tests written with **Hardhat**, **ethers.js**, and **Mocha / Chai**. Pairs with `foundry_test_project/` — the same contracts are covered there using Foundry's native Solidity tests.

## Stack

- **Solidity** (contracts: `Token`, `Lock`)
- **Hardhat** + **ethers.js** test runner
- **Mocha / Chai** for assertions
- **Hardhat Ignition** for declarative deployments

## What's covered

- **`Token.sol`** — ERC-20-ish token with `mint`, `transfer`, `approve`, `transferFrom`. Tests cover: balances, allowances, event emission (`Transfer`, `Approval`), and revert paths (insufficient balance / allowance).
- **`Lock.sol`** — standard Hardhat sample time-locked withdrawal. Tests cover deploy-time validation, `withdraw()` access control, and the happy-path release after `unlockTime`.

## Layout

```
hardhat_test_project/
├── contracts/
│   ├── Lock.sol
│   └── Token.sol
├── test/
│   ├── Lock.js
│   └── Token.js
├── ignition/                 # Hardhat Ignition deployment modules
├── hardhat.config.js
└── package.json
```

## Run

```bash
cd hardhat_test_project
npm install

# Run the full test suite
npx hardhat test

# With gas reporting
REPORT_GAS=true npx hardhat test

# Start a local node
npx hardhat node

# Deploy via Ignition (example)
npx hardhat ignition deploy ./ignition/modules/Lock.js
```
