# QA Automation Portfolio

[![API Tests](https://github.com/kaminomas/projects/actions/workflows/test.yml/badge.svg)](https://github.com/kaminomas/projects/actions/workflows/test.yml)

A personal portfolio of quality-engineering projects spanning **REST API testing**, **browser UI automation**, and **smart-contract testing on EVM chains**. Each sub-project is self-contained with its own dependencies, tests, and README.

> **Work in progress.** This repo documents a real, ongoing learning path — not a polished product. Modules are marked 🟢 / 🟡 / 🔴 so you can see exactly where each one stands.

---

## Modules

| Module | Stack | Status | Summary |
|---|---|---|---|
| [`api_test_project/`](./api_test_project) | Python · pytest · requests · Allure | 🟢 | End-to-end API tests against [restful-booker](https://restful-booker.herokuapp.com/) with a pluggable auth-strategy layer (Cookie / Bearer) and swappable password encryptors (Plain / MD5 / SHA256). Runs in CI. |
| [`ui_test_project/`](./ui_test_project) | Python · Selenium · Page Object Model · Docker Compose Selenium Grid | 🟡 | Remote-WebDriver setup with POM structure. Smoke test currently skipped in CI; runs locally once the Grid is up. |
| [`hardhat_test_project/`](./hardhat_test_project) | Solidity · Hardhat · ethers.js · Mocha / Chai | 🟢 | ERC-20-ish `Token` + `Lock` contracts with unit tests, event assertions, and revert-path coverage. |
| [`foundry_test_project/`](./foundry_test_project) | Solidity · Foundry (`forge`) | 🟢 | Same contracts tested with Foundry's native Solidity tests — including fuzz tests, `vm.prank`, `vm.expectRevert`, and `vm.assume`. |
| [`web3_lab/`](./web3_lab) | TypeScript · ethers v6 | 🟡 | Ad-hoc on-chain scripts (block number, balance lookups) against a public Sepolia RPC. Learning sandbox, not a test suite. |

Status legend: 🟢 stable & tested in CI · 🟡 works locally, partial or gated · 🔴 experimental / broken.

---

## Why this repo exists

Most QA portfolios show one framework. This one shows **one engineer's reasoning across three very different testing domains** — how contracts, HTTP APIs, and browser UIs each demand different trade-offs in test design, flakiness control, data setup, and reporting. The goal is to demonstrate:

- **Real coverage choices** — unit vs. integration vs. end-to-end, and when each pays off.
- **Strategy patterns over copy-paste** — e.g. the `api_test_project` auth layer is a pluggable strategy, not a hard-coded login.
- **Honest state** — what's green, what's flaky, what's half-built. No pretending.

---

## Quick start

Each module is independent. Open the sub-folder and follow its README. Typical flow:

```bash
# API tests (Python 3.11+)
cd api_test_project
pip install -r requirements.txt
# Start the mock API on :3001 first, then:
pytest tests/ -v

# Hardhat contracts
cd hardhat_test_project
npm install
npx hardhat test

# Foundry contracts
cd foundry_test_project
forge test -vv
```

## CI

GitHub Actions runs the API test suite on every push. See [`.github/workflows/test.yml`](./.github/workflows/test.yml).

## Contact

- GitHub: [@kaminomas](https://github.com/kaminomas)
- Email: _(add before publishing)_
- Upwork / LinkedIn: _(add before publishing)_

---

# 中文说明

一个质量工程作品集，涵盖 **REST API 接口测试**、**浏览器 UI 自动化**，以及 **EVM 智能合约测试**。每个子项目独立维护，包含各自的依赖、测试和 README。

> **持续完善中。** 本仓库记录的是真实、进行中的学习与实战路径，不是成品。每个模块用 🟢 / 🟡 / 🔴 清晰标注当前状态。

## 模块总览

| 模块 | 技术栈 | 状态 | 简介 |
|---|---|---|---|
| [`api_test_project/`](./api_test_project) | Python · pytest · requests · Allure | 🟢 | 基于 [restful-booker](https://restful-booker.herokuapp.com/) 的端到端接口测试，实现了可插拔的鉴权策略层（Cookie / Bearer）与可替换的密码加密器（Plain / MD5 / SHA256）。已接入 CI。 |
| [`ui_test_project/`](./ui_test_project) | Python · Selenium · Page Object Model · Docker Compose Selenium Grid | 🟡 | Remote WebDriver + POM 结构。冒烟用例在 CI 中跳过，本地启动 Grid 后可运行。 |
| [`hardhat_test_project/`](./hardhat_test_project) | Solidity · Hardhat · ethers.js · Mocha / Chai | 🟢 | `Token`（类 ERC-20）与 `Lock` 合约，覆盖单元测试、事件断言、异常路径。 |
| [`foundry_test_project/`](./foundry_test_project) | Solidity · Foundry (`forge`) | 🟢 | 用 Foundry 原生 Solidity 测试同一批合约，包含模糊测试、`vm.prank`、`vm.expectRevert`、`vm.assume` 等常用手段。 |
| [`web3_lab/`](./web3_lab) | TypeScript · ethers v6 | 🟡 | 链上脚本练习（查区块号、查余额），通过公网 Sepolia RPC 运行。定位为学习沙盒，不是测试套件。 |

状态标记：🟢 稳定，CI 中运行 · 🟡 本地可跑，部分跳过或需手动启动 · 🔴 实验性 / 待修复。

## 这个仓库存在的意义

大多数 QA 作品集只展示一种框架。这个仓库想展示的是**一个工程师在三类完全不同的测试领域里的思考方式**——合约、HTTP 接口、浏览器 UI，每一类在测试设计、稳定性控制、数据准备、结果报告上的权衡都不一样。核心诉求：

- **覆盖策略的取舍** —— 单元、集成、端到端各自的边界和成本。
- **用设计模式而不是复制粘贴** —— 比如 `api_test_project` 里的鉴权层是可插拔的策略类，而不是写死的登录流程。
- **诚实的状态标注** —— 哪里稳定、哪里会跳过、哪里还没做完，都直接写出来。

## 快速开始

各模块独立，进入对应目录按其 README 运行。典型流程：

```bash
# 接口测试（Python 3.11+）
cd api_test_project
pip install -r requirements.txt
# 先启动 :3001 上的 mock 服务，然后：
pytest tests/ -v

# Hardhat 合约
cd hardhat_test_project
npm install
npx hardhat test

# Foundry 合约
cd foundry_test_project
forge test -vv
```

## CI

每次 push 都会通过 GitHub Actions 跑接口测试套件，配置见 [`.github/workflows/test.yml`](./.github/workflows/test.yml)。

## 联系方式

- GitHub: [@kaminomas](https://github.com/kaminomas)
- Email: _（发布前补全）_
- Upwork / LinkedIn: _（发布前补全）_
