from random import choice

# Alice generiert eine zufällige Bitfolge und sendet sie an Bob
def generate_random_bits(length):
    return [choice([0, 1]) for _ in range(length)]

# Bob wählt zufällig eine Basis für jede empfangene Bitfolge
def choose_bases(bits, length):
    return [choice(['rectilinear', 'diagonal']) for _ in range(length)]

# Alice codiert jedes Bit in der gewählten Basis und sendet die Photonen an Bob
def encode_bits(bits, bases):
    photons = []
    for bit, basis in zip(bits, bases):
        if basis == 'rectilinear':
            photon = {'horizontal': bit, 'vertical': (bit + 1) % 2}
        else:
            photon = {'diagonal1': bit, 'diagonal2': (bit + 1) % 2}
        photons.append(photon)
    return photons

# Bob misst jedes Photon in der gewählten Basis und erhält die empfangenen Bits
def measure_photons(photons, bases):
    bits = []
    for photon, basis in zip(photons, bases):
        if basis == 'rectilinear':
            bit = photon['horizontal']
        else:
            bit = photon['diagonal1']
        bits.append(bit)
    return bits

# Alice und Bob vergleichen ihre Basen und verwerfen die Bits, die in unterschiedlichen Basen übertragen wurden
def discard_mismatched_bits(alice_bases, bob_bases, bits):
    return [bit for bit, alice_basis, bob_basis in zip(bits, alice_bases, bob_bases) if alice_basis == bob_basis]

# Das Hauptprogramm
def main():
    # Alice generiert eine zufällige Bitfolge
    alice_bits = generate_random_bits(10)
    
    # Bob wählt zufällig eine Basis für jede empfangene Bitfolge
    bob_bases = choose_bases(alice_bits, 10)
    
    # Alice codiert jedes Bit in der gewählten Basis und sendet die Photonen an Bob
    photons = encode_bits(alice_bits, bob_bases)
    
    # Bob misst jedes Photon in der gewählten Basis und erhält die empfangenen Bits
    bob_bits = measure_photons(photons, bob_bases)
    
    # Alice und Bob vergleichen ihre Basen und verwerfen die Bits, die in unterschiedlichen Basen übertragen wurden
    alice_bases = bob_bases
    alice_bits = discard_mismatched_bits(alice_bases, bob_bases, alice_bits)
    bob_bits = discard_mismatched_bits(alice_bases, bob_bases, bob_bits)
    
    # Alice und Bob vergleichen ihre Bitfolgen und verifizieren die Kommunikation
    if alice_bits == bob_bits:
        print('Die Quantenverschlüsselung war erfolgreich!')
    else:
        print('Die Quantenverschlüsselung ist fehlgeschlagen!')

if __name__ == '__main__':
    main()
