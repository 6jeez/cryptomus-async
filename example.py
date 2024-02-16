from cryptomus import create_invoice, get_invoice


# create invoice
async def create_invoice_example() -> None:
    invoice = await create_invoice("123123-invoice_id-123123", 100)
    print(invoice['result']['url'])


async def get_invoice_example() -> None:
    invoice = await get_invoice("123123-invoice_id-123123")
    
    if invoice['result']['status'] == 'paid':
        print('invoice is paid')
    else:
        print('invoice is not paid')
