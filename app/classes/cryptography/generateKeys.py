import classes.math.generateNumbers as gN

from Crypto.PublicKey import RSA

import random


def gen_rsa_keys_with_math():
    """
    Generate RSA keys with pure math.
    """
    p = random.choice(gN.prime_numbers(100, 1000))
    q = random.choice(gN.prime_numbers(100, 1000))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    # d = gN.modular_inverse(e, phi)


def gen_rsa_keys_with_pycryptodome():
    """
    Generate RSA keys with pycryptodome.
    """
    pr_key = RSA.generate(2048)
    pu_key = pr_key.publickey()

    private_key = pr_key.exportKey().decode("utf-8")
    public_key = pu_key.exportKey().decode("utf-8")

    return private_key, public_key
