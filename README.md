Creating and accepting Cryptomus payments asynchronously

**Example**

```python
import asyncio
from cryptomus import CryptoMusClient


# create invoice
async def create_invoice_example() -> None:
    client = CryptoMusClient()
    invoice = await client.create_invoice("123123-invoice_id-123123", 100)
    print(invoice['result']['url'])
```

```python
import asyncio
from cryptomus import CryptoMusClientprint('invoice is not paid')


# get invoice
async def get_invoice_example() -> None:
    client = CryptoMusClient()
    invoice = await client.get_invoice("123123-invoice_id-123123")
    
    if invoice['result']['status'] == 'paid':
        print('invoice is paid')
    else:
        print('invoice is not paid')
```