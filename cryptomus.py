import json 
import hashlib
import base64
from typing import Dict, Any

from aiohttp import ClientSession

from config import UUID, API_KEY


class CryptoMusClient:
    def __init__(self):
        pass
    
    def generate_headers(self, data: str) -> Dict[str, Any]:
        sign = hashlib.md5(
            base64.b64encode(data.encode('ascii')) + API_KEY.encode('ascii')
        ).hexdigest()

        return {"merchant": UUID, "sign": sign, "Content-Type": "application/json"}

    async def create_invoice(self, invoice_id, amount) -> dict:
        async with ClientSession() as session:
            json_data = {
                "amount": int(amount),
                "order_id": invoice_id.replace(' ', '-'),
                "currency": "USDT",
                "network": "TRC20",
                "lifetime": 3600,  # 1 hour(in seconds)
            }
            json_dump = json.dumps(json_data)
            
            response = await session.post(
                "https://api.cryptomus.com/v1/payment",
                data=json_dump,
                headers=self.generate_headers(json_dump)
            )

            return await response.json()

    async def get_invoice(self, invoice_id) -> dict:
        async with ClientSession() as session:
            json_data = {'uuid': invoice_id}
            json_dump = json.dumps(json_data)
            response = await session.post(
                "https://api.cryptomus.com/v1/payment/info",
                data=json_dump,
                headers=self.generate_headers(json_dump)
            )

            return await response.json()
