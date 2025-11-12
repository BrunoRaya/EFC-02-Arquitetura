# adapter_pattern.py
# Implementação do padrão Adapter para adaptar uma API externa de entrega ao formato interno
from typing import Dict, Any


# Simulação de serviço externo com interface incompatível
class ExternalDeliveryService:
    def create_shipment(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        print("[ExternalDelivery] Criando envio com payload externo:", payload)
        return {"tracking_id": "TRK123456", "eta_minutes": 45}


# Interface esperada pelo sistema interno
class DeliveryInterface:
    def send(self, order_id: int, address: str) -> Dict[str, Any]:
        raise NotImplementedError


# Adapter que converte a chamada interna para a externa
class ExternalDeliveryAdapter(DeliveryInterface):
    def __init__(self, external_service: ExternalDeliveryService):
        self.external = external_service

    def send(self, order_id: int, address: str) -> Dict[str, Any]:
        payload = {
            "recipient": {"order_id": order_id, "address": address},
            "parcel": {"weight_kg": 1.0}
        }
        result = self.external.create_shipment(payload)
        adapted = {
            "order_id": order_id,
            "tracking": result.get("tracking_id"),
            "eta_minutes": result.get("eta_minutes")
        }
        print(f"[AdapterDelivery] Envio adaptado para pedido #{order_id}: tracking={adapted['tracking']}")
        return adapted
