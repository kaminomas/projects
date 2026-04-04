const { expect } = require("chai");

describe("Token", function () {
    let token;

    beforeEach(async function () {
        const Token = await ethers.getContractFactory("Token");
        token = await Token.deploy();
    });

    it("test owner", async function () {
        const [owner] = await ethers.getSigners();
        expect(await token.owner()).to.equal(owner.address);
    });

    it("test mint", async function () {
        const [owner] = await ethers.getSigners();
        await token.mint(owner.address, 100);
        expect(await token.balanceOf(owner.address)).to.equal(100);
    });
});


