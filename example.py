import asyncio
from cryptomus import CryptoMusClient


# create invoice
async def create_invoice_example() -> None:
    client = CryptoMusClient()
    invoice = await client.create_invoice("123123-invoice_id-123123", 100)
    print(invoice['result']['url'])


# get invoice
async def get_invoice_example() -> None:
    client = CryptoMusClient()
    invoice = await client.get_invoice("123123-invoice_id-123123")
    
    if invoice['result']['status'] == 'paid':
        print('invoice is paid')
    else:
        print('invoice is not paid')


async def main() -> None:
    await create_invoice_example()
    await get_invoice_example()


if __name__ == "__main__":
    asyncio.run(main())
