import hashlib
import random
import string
import datetime

def generate_random_wallet():
    """Генерирует случайный криптокошелёк (фейковый)"""
    return '0x' + ''.join(random.choices('abcdef' + string.digits, k=40))

def verify_wallet_address(address):
    """Простейшая проверка на валидность адреса (эмуляция)"""
    if not address.startswith("0x") or len(address) != 42:
        return False
    return all(c in string.hexdigits for c in address[2:])

def generate_address_proof(address):
    """Генерирует 'доказательство владения' — хэш + подпись (эмуляция)"""
    timestamp = datetime.datetime.utcnow().isoformat()
    raw = f"{address}|{timestamp}|secret_key_simulated"
    return hashlib.sha256(raw.encode()).hexdigest()

def main():
    address = generate_random_wallet()
    print(f"🔐 Сгенерирован адрес: {address}")

    if verify_wallet_address(address):
        print("✅ Адрес валиден")
        proof = generate_address_proof(address)
        print(f"📎 Псевдо-доказательство владения: {proof}")
    else:
        print("❌ Недействительный адрес")

if __name__ == "__main__":
    main()
