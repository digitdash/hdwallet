#!/usr/bin/env python3
# HD wallet generator - m/44'/0'/0'/0/0
# By Dash @ Gamba

from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL

import json

hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
hdwallet.from_entropy(entropy=hdwallet.generate_entropy(strength=256), language="english", passphrase=None)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, hardened=True)
hdwallet.from_index(0, hardened=True)
hdwallet.from_index(0)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Output
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
