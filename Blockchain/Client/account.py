import sys
sys.path.append("/Bitcoin")
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
from Blockchain.Backend.utils.util import hash160, hash256

import secrets

class account:
    def createKeys(self):
        Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
        Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

        G = Sha256Point(Gx, Gy)

        privateKey = secrets.randbits(256)
        unCompressPublicKey = privateKey * G
        xPoint = unCompressPublicKey.x
        yPoint = unCompressPublicKey.y

        if yPoint.num % 2 == 0:
            compressKey = b'\x02' + xPoint.num.to_bytes(32, 'big')
        else:
            compressKey = b'\x03' + xPoint.num.to_bytes(32, 'big')

        hsh160 = hash160(compressKey)
        "Prefix for mainnet"
        main_prefix = b'\x00'

        newAddr = main_prefix + hsh160

        "Checksum"
        checksum = hash256(newAddr)[:4]

        newAddr = newAddr + checksum
        BASE58_ALPHABET = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        count = 0

        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break

        num = int.from_bytes(newAddr, 'big')
        prefix = '1' * count

        result = ''

        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result

        PublicAddress = prefix + result

        print(f'Private key is {privateKey}')
        print(f'Public address is {PublicAddress}')



if __name__ == "__main__":
    acct = account()
    acct.createKeys()