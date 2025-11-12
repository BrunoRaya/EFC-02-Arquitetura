# payment_strategy.py
# Implementação do padrão Strategy: permite trocar algoritmos de pagamento em tempo de execução
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float, details: dict) -> bool:
        """Executa o pagamento. Retorna True se sucesso, False caso contrário."""


class PixPayment(PaymentStrategy):
    def pay(self, amount: float, details: dict) -> bool:
        chave = details.get("pix_key")
        if not chave:
            print("[Pix] Falha: chave Pix ausente.")
            return False
        print(f"[Pix] Pagamento de R$ {amount:.2f} via Pix (chave={chave}) confirmado.")
        return True


class CardPayment(PaymentStrategy):
    def pay(self, amount: float, details: dict) -> bool:
        card = details.get("card_number", "")
        if len(card) < 12:
            print("[Cartão] Falha: número do cartão inválido.")
            return False
        print(f"[Cartão] Pagamento de R$ {amount:.2f} com cartão final {card[-4:]} aprovado.")
        return True


class BoletoPayment(PaymentStrategy):
    def pay(self, amount: float, details: dict) -> bool:
        print(f"[Boleto] Boleto gerado para R$ {amount:.2f}. Status: aguardando pagamento.")
        return True
