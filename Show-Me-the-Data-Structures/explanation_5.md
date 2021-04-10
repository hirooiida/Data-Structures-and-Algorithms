# Blockchain
## Reason
BlockChain only keep ```tail``` for its append operation. Each block is only linked by ```previous_hash``` property of ```Block``` class.

## Efficiency
Time complexity is O(1) for appending new data. Time complexity is O(n) for ```print``` function of BlockChain since it is dependent on the chain length.

Space efficiency is O(n). ```BlockChain``` stores one ```Block``` instance for each data.
