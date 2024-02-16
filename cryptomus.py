import json 
import hashlib
import base64
from typing import Dict, Any

from aiohttp import ClientSession

from config import UUID, API_KEY


def generate_headers(data: str) -> Dict[str, Any]:
    sign = hashlib.md5(
        base64.b64encode(data.encode('ascii')) + API_KEY.encode('ascii')
    ).hexdigest()

    return {"merchant": UUID, "sign": sign, "Content-Type": "application/json"}


async def create_invoice(invoice_id, amount) -> dict:
    """
    Creates an invoice for a given invoice ID and amount.

    Args:
        invoice_id (str): The ID of the invoice.
        amount (float): The amount of the invoice.

    Returns:
        dict: The response JSON containing the invoice details.
    """
    async with ClientSession() as session:
        json_dump = json.dumps(
            data = {
            "amount": int(amount),
            "order_id": invoice_id,  # should not contain spaces, use - instead of spaces
            "currency": "USDT",
            "network": "TRC20",
            "lifetime": 3600,  # 1 hour(in seconds)
            }
        )
        
        response = await session.post(
            "https://api.cryptomus.com/v1/payment",
            data=json_dump,
            headers = generate_headers(json_dump)
        )

        return await response.json()


async def get_invoice(invoice_id) -> dict:
    async with ClientSession() as session:
        json_dump = json.dumps({'uuid': invoice_id})
        response = await session.post(
            "https://api.cryptomus.com/v1/payment/info",
            data=json_dump,
            headers=generate_headers(json_dump)
        )

        return await response.json()
