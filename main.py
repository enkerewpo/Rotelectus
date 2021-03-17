# -*- coding:utf-8 -*-

import hanlp
import json


def build():
    in_file = open('input.txt', 'r')
    input_str = str(in_file.read())

    out_file = open('output.json', 'w')
    HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)
    out_str = str(HanLP([input_str]))

    HanLP([input_str]).pretty_print()

    out_file.write(out_str)

    in_file.close()
    out_file.close()


if __name__ == '__main__':

    flag = 1
    if flag:
        build()

    json_file = open('output.json')
    data = json.load(json_file)
    cur = 0
    for p in data['dep']:
        for q in p:
            to = q[0] - 1
            rel = q[1]
            if (rel == 'nsubj') \
                    and (data['pos'][0][to] == 'NOUN' or data['pos'][0][to] == 'PROPN') \
                    and (data['pos'][0][cur] == 'NOUN' or data['pos'][0][cur] == 'PROPN'):
                print(data['tok'][0][to] + '->' + data['tok'][0][cur])
            cur += 1
    json_file.close()