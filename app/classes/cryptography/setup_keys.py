import data.basicData as bD
import classes.cryptography.generateKeys as gKs


def setup_pycryptodome_keys():
    bD.pr_key, bD.pub_key = gKs.gen_rsa_keys_with_pycryptodome()
    print(bD.pr_key, bD.pub_key)
