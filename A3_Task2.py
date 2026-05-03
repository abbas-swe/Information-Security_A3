# ECC Parameters
a = 2
b = 2
p = 17

# Base Point
G = (5, 1)

# Modular Inverse Function
def mod_inverse(k, p):
    for i in range(1, p):
        if (k * i) % p == 1:
            return i
    return None

# Point Addition
def point_add(P, Q):
    if P == Q:
        return point_double(P)

    x1, y1 = P
    x2, y2 = Q

    slope = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)

# Point Doubling
def point_double(P):
    x1, y1 = P

    slope = ((3 * x1**2 + a) * mod_inverse(2 * y1, p)) % p

    x3 = (slope**2 - 2 * x1) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)

# Scalar Multiplication
def scalar_multiply(k, P):
    result = P

    for _ in range(k - 1):
        result = point_add(result, P)

    return result

# Key Generation
private_key = 4
public_key = scalar_multiply(private_key, G)

print("Private Key:", private_key)
print("Public Key:", public_key)

#Message Example
message = 6
M = scalar_multiply(message, G)

# Encryption
k = 3

C1 = scalar_multiply(k, G)
C2 = point_add(M, scalar_multiply(k, public_key))

print("\nEncrypted Message:")
print("C1:", C1)
print("C2:", C2)

# Decryption
shared_secret = scalar_multiply(private_key, C1)

neg_shared_secret = (
    shared_secret[0],
    (-shared_secret[1]) % p
)

recovered_message = point_add(C2, neg_shared_secret)

print("\nRecovered Message Point:")
print(recovered_message)