# web3_lab 🟡

A **TypeScript + ethers v6** sandbox for on-chain scripting against public testnets. Not a test suite — this is where I experiment with RPC calls, provider plumbing, and ethers v6 idioms before pulling the useful bits back into the test projects.

## Stack

- **TypeScript**, **ethers v6**
- **tsx** for zero-build script running
- **dotenv** for the RPC URL
- Package manager: **pnpm**

## What's in here

- `scripts/get_block_number.ts` — simplest "is the provider alive?" probe.
- `scripts/get_balance.ts` — queries the ETH balance of vitalik.eth (`0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`) and prints it in wei and ETH.

## Run

```bash
cd web3_lab
pnpm install

# 1. Provide an RPC URL (Sepolia, mainnet, whatever you have)
cp .env.example .env    # or create .env manually
# RPC_URL=https://sepolia.infura.io/v3/<YOUR_KEY>

# 2. Run a script
pnpm tsx scripts/get_block_number.ts
pnpm tsx scripts/get_balance.ts
```

## Why it's 🟡

No tests yet — scripts print to stdout, nothing is asserted. Next steps when this matures:

- Add `vitest` and assert on return shapes.
- Wrap the provider setup in a reusable `getProvider()` helper.
- Promote the useful helpers into `hardhat_test_project/` so contract tests can hit real testnets too.
