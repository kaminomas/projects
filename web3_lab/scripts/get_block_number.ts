import { config } from "dotenv";
import { ethers } from "ethers";

config();

async function main() {
  const rpcUrl = process.env.RPC_URL;

  if (!rpcUrl) {
    throw new Error("RPC_URL is not set in .env");
  }

  const provider = new ethers.JsonRpcProvider(rpcUrl);
  const blockNumber = await provider.getBlockNumber();

  console.log("Current block number:", blockNumber);
}

main().catch((err) => {
  console.error("Script failed:", err);
  process.exit(1);
});