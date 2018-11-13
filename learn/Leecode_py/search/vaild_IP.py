
class VaildIP():
    def __init__(self, string):
        self.s = string
        self.vaild_IPs = []
        self.IP_length = 4

    def is_item_correct(self, item):
        if len(item) > 3 or len(item) == 0:
            return False
        if item[0] == '0' and len(item) != 1:
            return False
        if int(item) > 255 or int(item) < 0:
            return False

        return True

    def vaild_IP(self, seq, start, end, item_num=1):

        if item_num == self.IP_length - 1:
            if self.is_item_correct(self.s[start:end]) and self.is_item_correct(self.s[end:]):
                seq.append(self.s[start:end])
                seq.append(self.s[end:])
                self.vaild_IPs.append(seq)
            return
        if self.is_item_correct(self.s[start:end]):
            seq.append(self.s[start:end])
            for i in range(3):
                sequence = seq.copy()
                self.vaild_IP(sequence, end, end + i + 1, item_num +
                              1)


def vaild_ips(string):
    for letter in string:
        if letter not in '0123456789':
            return []

    vip = VaildIP(string)
    for i in range(3):
        seq = []
        vip.vaild_IP(seq.copy(), 0, i + 1)
    return vip.vaild_IPs


if __name__ == "__main__":
    print(vaild_ips('25525511135'))
