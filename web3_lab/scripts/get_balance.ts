import { config } from "dotenv";
import { ethers } from "ethers";

config();

async function main() {
  const rpcUrl = process.env.RPC_URL;

  if (!rpcUrl) {
    throw new Error("RPC_URL is not set in .env");
  }

  const address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045";

  const provider = new ethers.JsonRpcProvider(rpcUrl);
  const balance = await provider.getBalance(address);

  console.log("Address:", address);
  console.log("Balance (wei):", balance.toString());
  console.log("Balance (ETH):", ethers.formatEther(balance));
}

main().catch((err) => {
  console.error("Script failed:", err);
  process.exit(1);
});