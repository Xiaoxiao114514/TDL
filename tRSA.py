# coding: UTF-8
from __future__ import print_function
import rsa


class RSA(object):
    @staticmethod
    def rsa_encrypt(plaintext):
        """
        输入明文、生成公钥、私钥
        公钥对明文进行加密、字符串加密
        :return:加密结果及私钥
        """
        pub_key, priv_key = rsa.newkeys(1024)
        print(pub_key)
        print(priv_key)
        plaintext = plaintext.encode()  # the message to encrypt. Must be a byte string no longer than``k-11`` bytes
        ciphertext = rsa.encrypt(plaintext, pub_key)
        return ciphertext, priv_key

    @staticmethod
    def rsa_decrypt(ciphertext, priv_key):
        """
        传参私钥和加密的明文
        :param ciphertext:
        :param priv_key:
        :return:解密结果
        """
        plaintext = rsa.decrypt(ciphertext, priv_key)
        plaintext = plaintext.decode()
        return plaintext
