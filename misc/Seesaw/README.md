# 'Seesaw'

This challenge uses the ethereum ctf challenge framework developed by samczsun at paradigm.xyz

# I'm already hosting at  167.172.159.91 .

Just tell participants to `nc 167.172.159.91 31337`

The box is overprovisioned so I do not foresee performance issues

## Installing

### Prerequisites

* Docker
* [mpwn](https://github.com/lunixbochs/mpwn)
* Python 3

### Configuration

You'll need to set the following environment variables:
* `ETH_RPC_URL` to a valid Ethereum JSON-RPC endpoint
* `PYTHONPATH` to point to mpwn

You'll also need to manually install the following:
* `pip install yaml ecdsa pysha3 web3 cairo-lang`

## Usage

### Build everything

```bash
docker buildx build --platform linux/amd64 -t mytag .
```

### Run a challenge

Running a challenge will open a port which users will `nc` to. For Ethereum/Starknet related
challenges, an additional port must be supplied so that users can connect to the Ethereum/Starknet
node

```
./run.sh mytag 31337 8545
```

On another terminal:

```
nc localhost 31337
```

When prompted for the ticket, they will need to solve a PoW. This ticket should NOT be shared between teams, it's a secret.

```
$ nc localhost 31337
1 - launch new instance
2 - kill instance
3 - get flag
action? 1
ticket please: ticket

your private blockchain has been deployed
it will automatically terminate in 30 minutes
here's some useful information
```

### How to solve it

See solve.sh, basically just deploy Exploit.sol contract and run it. Constructor expects 100 eth and parameter is setup contract address
