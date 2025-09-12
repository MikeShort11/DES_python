# Des algorithim in python for computer security

pc_1 = [ #key permutation table one
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4 
]
pc_2 = [ #key permutation table 2
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]



def hex_to_bits(hex_text):
    byte_text = bytes.fromhex(hex_text)
    result = []
    for byte in byte_text:
        bits = format(byte, '08b')
        result.extend((int(b) for b in bits))
    return result

def permute(bit_array:list, table:list):
    result = []
    for i in table:
        result.append(bit_array[i - 1])
    return result;

def make_keys(hex_key):
    bin_key = hex_to_bits(hex_key)
    #print(bin_key)
    pemutation_1 = permute(bin_key, pc_1)
    #print(pemutation_1)
    c = pemutation_1[:28]
    d = pemutation_1[28:]
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    keys_list = []
    for s in shifts:
        #shift 1 or 2 places left
        c = c[s:] + c[:s]
        d = d[s:] + d[:s]
        #combine, permute and add to list
        combined = c + d
        keys_list.append(permute(combined, pc_2))
    return keys_list

def main():
    #plaintext = input("Enter plaintext to encrypt: ")
    #hex_key = input("Enter key to use: ")

    plaintext = "0123456789ABCDEF"
    hex_key = "133457799BBCDFF1"
    print(f"plaintext: {plaintext}\nkey: {hex_key}")

    binaray_plaintext = hex_to_bits(plaintext)
    keys_list = make_keys(hex_key)
    print(f"Final keys list: {keys_list}")

if __name__ == "__main__":
    main()

