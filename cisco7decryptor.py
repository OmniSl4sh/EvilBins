def cisco_type7_decrypt(enc):
    xlat = [
        0x64, 0x73, 0x66, 0x64, 0x3B, 0x6B, 0x66, 0x6F,
        0x41, 0x2C, 0x2E, 0x69, 0x79, 0x65, 0x77, 0x72,
        0x6B, 0x6C, 0x64, 0x4A, 0x4B, 0x44, 0x48, 0x53,
        0x55, 0x42
    ]
    try:
        start = int(enc[:2])
        enc = enc[2:]
        res = ''
        for i in range(0, len(enc), 2):
            res += chr(int(enc[i:i+2], 16) ^ xlat[(start + i//2) % len(xlat)])
        return res
    except Exception as e:
        return f"[ERROR decoding '{enc}']: {e}"

def decrypt_file(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            for idx, line in enumerate(lines, 1):
                decrypted = cisco_type7_decrypt(line)
                print(f"[Line {idx}] {line} => {decrypted}")
    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python cisco7_bulk_decrypt.py <encrypted_passwords_file>")
        sys.exit(1)

    decrypt_file(sys.argv[1])
