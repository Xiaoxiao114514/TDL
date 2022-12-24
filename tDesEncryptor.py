# coding: UTF-8
"""
DES加密器
该类可实现字符串的加密与解密
"""


class DesEncryptor(object):
    # 初始化函数
    def __init__(self):
        """
        请查阅 helpDoc()
        variable: 变量
        eFunctions: 公开函数
        hFunctions: 隐藏函数
        example: 示例
        """
        self.__key = None
        self.__ciphertext = None
        self.__plaintext = None

    # 移位函数
    @staticmethod
    def shift(s, n):
        """

        :param s: 需要移位的字符串
        :param n: 需要移动的位数
        :return:
        """
        return s[n:] + s[:n]

    @staticmethod
    # 异或函数
    def xor(a, b):
        """
        异或函数
        :param a:
        :param b:等长的字符串
        return：a和b异或后的结果
        """
        t = zip(a, b)
        s = [(int(i) + int(j)) % 2 for i, j in t]
        S = ''
        for i in s:
            S = S + str(i)
        return S

    # 明文字符串转二进制
    @staticmethod
    def get_p_bin(texts):
        """
        字符串转二进制
        Text：字符串
        return 字符串对应的二进制的编码
        """
        Text_bin = ''
        for Text in texts:
            s = ord(Text)
            s_bin = '{:016b}'.format(s)
            Text_bin = Text_bin + s_bin
        return Text_bin

    # 密文字符串转二进制
    @staticmethod
    def get_c_bin(Texts):
        """字符串转二进制
        Text：字符串
        return 字符串对应的二进制的编码
        """
        Text_bin = ''
        for Text in Texts:
            s = ord(Text)
            s_bin = '{:08b}'.format(s)
            Text_bin = Text_bin + s_bin
        return Text_bin

    # 二进制转字符函数
    @staticmethod
    def bin_str(s):
        """获取16位的01串，返回对应的汉字"""
        # noinspection PyBroadException
        try:
            return chr(int(s, 2))
        except:
            return -1

    # 十进制转二进制
    @staticmethod
    def ten_to_two(n):
        """
        返回小于16的数转换为四位二进制数(字符串)
        n:小于16的十进制数
        return：四位的二进制数，不足四位在前方补零
        """
        n2 = bin(n)[2:]
        num = len(bin(n)[2:])
        if num >= 4:
            return n2
        for i in range(4 - num):
            n2 = '0' + n2
        return n2

    # PC置换
    @staticmethod
    def pc(s, flag):
        PC1 = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4]
        PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
               15, 6, 21, 10, 23, 19, 12, 4,
               26, 8, 16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55, 30, 40,
               51, 45, 33, 48, 44, 49, 39, 56,
               34, 53, 46, 42, 50, 36, 29, 32]
        S = ''
        if flag == 1:
            for i in PC1:
                S = S + s[i - 1]
        if flag == 2:
            for i in PC2:
                S = S + s[i - 1]
        return S

    # 密钥生成器
    def get_sk(self, Text):  # 获取密钥
        shift_num = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        k = Text
        # 请输入密钥（四个汉字）
        k_bin = self.get_p_bin(k)
        k_bin = self.pc(k_bin, 1)  # PC_1置换
        K = []
        # print('k_bin=',k_bin)
        num = 0
        for i in range(16):
            num = num + 1
            k_bin = self.shift(k_bin[:28], shift_num[i]) + self.shift(k_bin[28:], shift_num[i])  # 分组移位
            K.append(self.pc(k_bin, 2))  # PC_2置换，并记录
            if num >= 4:
                continue
        self.__key = K

    # 获取明文字符串
    def get_plaintext(self, Text):
        """获取需要加密的明文并换成二进制形式"""
        mText = Text
        mText_bin = []
        M = self.get_p_bin(mText)
        i = 0
        for i in range(int(len(M) / 64)):  # 四字一组
            mText_bin.append(M[64 * i:64 * (1 + i)])
        i = i
        if len(M) > 64:
            mText_bin.append(M[64 * (1 + i):] + (64 - len(M[64 * (1 + i):])) * '0')  # 字多于于四个时，末位不足四位
        elif len(M) < 64:
            mText_bin.append(M + (64 - len(M)) * '0')  # 字少于四个时
        return mText_bin  # 返回二进制代码列表

    global key

    # 获取密文字符串
    def get_ciphertext(self, Text, flag):
        global key
        mText = Text
        m_bin = []
        M = ''
        if flag == 0:
            M = self.get_c_bin(mText)
        elif flag == 2:
            for j in Text.split(' ')[:-1]:
                if len(j) < 8:
                    M = M + '0' * (16 - len(j)) + j
                else:
                    M = M + j
        elif flag == 16:
            for j in Text.split(' ')[:-1]:
                if len(bin(int(j, 16))[2:]) < 8:
                    M = M + '0' * (8 - len(bin(int(j, 16))[2:])) + bin(int(j, 16))[2:]
                else:
                    M = M + bin(int(j, 16))[2:]
        flag = 0
        for key in range(int(len(M) / 64)):  # 四字一组
            m_bin.append(M[64 * key:64 * (1 + key)])
            flag = 1
        if len(M) % 64 > 0:
            m_bin.append(M[64 * (1 + key):] + (64 - len(M[64 * (1 + key):])) * '0')  # 字多于于四个时，末位不足四位
        elif flag == 0:
            m_bin.append(M + (64 - len(M)) * '0')  # 字少于四个时
        return m_bin  # 返回二进制代码列表flag

    # s盒中取数函数
    @staticmethod
    def get_s(h, listing, n):
        """
        获取s盒中的数
        h：行
        l：列
        n：第n+1个盒
        返回指定s盒的第h行第j列的数
        """
        s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
              0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
              4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
              15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
              3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
              0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
              13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
              13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
              13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
              1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
              13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
              10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
              3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
              14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
              4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
              11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
              10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
              9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
              4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
              13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
              1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
              6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
              1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
              7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
              2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        if n == 0:
            return s1[h * 16 + listing]
        if n == 1:
            return s2[h * 16 + listing]
        if n == 2:
            return s3[h * 16 + listing]
        if n == 3:
            return s4[h * 16 + listing]
        if n == 4:
            return s5[h * 16 + listing]
        if n == 5:
            return s6[h * 16 + listing]
        if n == 6:
            return s7[h * 16 + listing]
        if n == 7:
            return s8[h * 16 + listing]

    # P置换
    @staticmethod
    def exchange_p(a):
        """
        对得到的数据进行P置换
            a：需要进行P置换的字符串
            return 进行P置换后的字符串
        """
        p = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]
        f = ''
        for i in p:
            f = f + a[i - 1]
        return f

    # f函数
    def function(self, r, keyPlus):
        """
        f函数
        """
        # 扩张函数
        e = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]
        r_e = ''  # 初始化扩张后R

        for i in e:
            r_e = r_e + r[i - 1]
        s = self.xor(r_e, keyPlus)
        # 通过s盒进行压缩
        f = ''
        for i in range(8):
            h = int(s[0 + 6 * i]) * 2 + int(s[5 + 6 * i])  # 行
            listing = int(s[1 + 6 * i]) * 8 + int(s[2 + 6 * i]) * 4 + int(s[3 + 6 * i]) * 2 + int(s[4 + 6 * i])  # 列
            f = f + self.ten_to_two(self.get_s(h, listing, i))
        # 置换P
        f_p = self.exchange_p(f)
        return f_p

    # IP置换
    @staticmethod
    def exchange_ip(s, n):
        """
        IP置换
        S:需要置换的字符串
        n：置换参数，0为初始置换，1为逆初始置换
        return ：进行置换后的字符串
        """
        ip = [58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7]

        ip_ = [40, 8, 48, 16, 56, 24, 64, 32,
               39, 7, 47, 15, 55, 23, 63, 31,
               38, 6, 46, 14, 54, 22, 62, 30,
               37, 5, 45, 13, 53, 21, 61, 29,
               36, 4, 44, 12, 52, 20, 60, 28,
               35, 3, 43, 11, 51, 19, 59, 27,
               34, 2, 42, 10, 50, 18, 58, 26,
               33, 1, 41, 9, 49, 17, 57, 25]
        S = ''
        if n == 0:
            for i in ip:
                S = S + s[i - 1]
        if n == 1:
            for i in ip_:
                S = S + s[i - 1]
        return S

    # 加密函数
    def encryption(self, Text):
        nKey = self.__key
        cpy = []  # 密文
        self.__plaintext = self.get_plaintext(Text)
        for mp in self.__plaintext:
            mp = self.exchange_ip(mp, 0)  # ip置换
            L = mp[:32]
            R = mp[32:]
            for j in range(16):  # 16轮迭代
                T = L
                L = R
                R = self.xor(T, self.function(R, nKey[j]))
            cpy.append(self.exchange_ip(R + L, 1))
        self.__ciphertext = cpy
        return cpy

    # 解密函数
    def dencryption(self, Text, flag):
        """
        flag=0为字符串，flag=2为二进制串，flag=16为十六进制
        """
        nKey = self.__key
        M = []  # 译文容器
        self.__ciphertext = self.get_ciphertext(Text, flag)
        for mCip in self.__ciphertext:
            mCip = self.exchange_ip(mCip, 0)  # ip置换
            L = mCip[:32]
            R = mCip[32:]
            for j in range(16):  # 16轮迭代
                T = L
                L = R
                R = self.xor(T, self.function(R, nKey[15 - j]))
            M.append(self.exchange_ip(R + L, 1))
        self.__plaintext = M
        return M

    # 以数字形式展示
    def showc_in_num(self, n):
        """
        n代表进制，目前仅支持2进制和16进制
        """
        cStr = ''
        s_hex = ''
        for i in self.__ciphertext:
            cStr = cStr + i
        if n == 2:
            for i in range(int(len(cStr) / 8)):
                s_hex = s_hex + cStr[8 * i:8 + 8 * i] + ' '
            return s_hex
        elif n == 16:
            s_hex = ''
            for i in range(int(len(cStr) / 8)):
                s_hex = s_hex + str(hex(int(cStr[8 * i:8 + 8 * i], 2))) + ' '
            return s_hex
        else:
            return '请期待后续版本，感谢您的信赖'

    # 明文以文字形式展示
    def show_mtext(self):
        """
        明文
        """
        M = self.__plaintext
        m_text = ''
        for Text in M:
            for i in range(4):
                if Text[i * 16:16 * (1 + i)] != '0' * 16:
                    m_text = m_text + self.bin_str(Text[i * 16:16 * (1 + i)])
        return m_text

    # 密文以文字形式展示
    def show_ctext(self):
        """密文"""
        M = self.__ciphertext
        m_text = ''
        for Text in M:
            for i in range(8):
                m_text = m_text + self.bin_str(Text[i * 8:8 * (1 + i)])
        return m_text

    @staticmethod
    def helpDoc(help_id="all"):
        variable = """
变量:
    密钥 self.__Key
    明文 self.__Plaintext
    密文 self.__Ciphertext
        """

        eFunctions = """
公开函数:
    加密函数 Encryption(self)
    解密函数 Dencryption(self)
    以数字形式展示 ShowC_in_num(self,n)
    明文以文字形式展示 Show_Text(self,flag)
    密文以文字形式展示 Show_text(self,flag)
        """

        hFunctions = """
隐藏函数: (不推荐使用)
    移位函数 _Shift(self,s, n)
    异或函数 _Xor(self,a, b)
    明文字符串转二进制 _Get_Bin(self,Texts)
    密文字符串转二进制 _Get_bin(self,Texts)
    二进制转字符函数 _Bin_Str(self,s)
    十进制转二进制 _Ten_To_Two(self,n)
    PC置换 _PC(self,s, flag)
    密钥生成器 _Get_Sk(self)
    获取明文字符串 _Get_Plaintext(self)
    获取密文字符串 _Get_Ciphertext(self)
    s盒中取数函数 _Get_S(self,h, l, n)
    P置换 _Exchange_P(self,A)
    f函数 _Function(self,R, K)
    IP置换 _Exchange_IP(self,s, n)
        """

        example = """
示例:
    D = DesEncryptor()

    text = '我是明文'
    key = '我是密钥'

    D.get_sk(key)
    D.encryption(text)
    D.dencryption(c, 0)

    c = D.show_ctext()
    m = D.show_mtext()

    print('密文：', c)
    print('明文：', m)
        """

        if help_id == "all":
            print(variable)
            print(eFunctions)
            print(hFunctions)
            print(example)
        elif help_id == "variable":
            print(variable)
        elif help_id == "eFunctions":
            print(eFunctions)
        elif help_id == "hFunctions":
            print(hFunctions)
        elif help_id == "example":
            print(example)
