# Bob wählt zufällig eine Basis für jede empfangene Bitfolge und sendet seine Wahl an Alice
def choose_bases(length):
    return [choice(['rectilinear', 'diagonal']) for _ in range(length)]

# Alice sendet die Basen zurück
def send_bases(bases):
    return bases

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

# Bob vergleicht seine Basen mit den von Alice erhaltenen Basen und verwerfen die Bits, die in unterschiedlichen Basen übertragen wurden
def discard_mismatched_bits(alice_bases, bob_bases, bits):
    return [bit for bit, alice_basis, bob_basis in zip(bits, alice_bases, bob_bases) if alice_basis == bob_basis]

# Das Hauptprogramm
def main():
    # Alice generiert eine zufällige Bitfolge
    alice_bits = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    
    # Bob wählt zufällig eine Basis für jede empfangene Bitfolge und sendet seine Wahl an Alice
    bob_bases = choose_bases(10)
    alice_bases = send_bases(bob_bases)
    
    # Alice codiert jedes Bit in der gewählten Basis und sendet die Photonen an Bob
    photons = encode_bits(alice_bits, alice_bases)
    
    # Bob misst jedes Photon in der gewählten Basis und erhält die empfangenen Bits
    bob_bits = measure_photons(photons, bob_bases)
    
    # Bob vergleicht seine Basen mit den von Alice erhaltenen Basen und verwerfen die Bits, die in unterschiedlichen Basen übertragen wurden
    alice_bits = discard_mismatched_bits(alice_bases, bob_bases, alice_bits)
    bob_bits = discard_mismatched_bits(alice_bases, bob_bases, bob_bits)
    
    # Bob hat nun eine Teilmenge der ursprünglichen Bitfolge von Alice und kann diese entschlüsseln
    decrypted_bits = bob_bits
    print('Entschlüsselte Bitfolge:', decrypted_bits)

if __name__ == '__main__':
    main()
