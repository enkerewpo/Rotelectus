# -*- coding:utf-8 -*-

import hanlp
import json

input_str = ""

def build():
    """ Build the pos network from pretrained sets
    """

    out_file = open('output.json', 'w')
    HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)
    out_str = str(HanLP([input_str]))

    out_file.write(out_str)
    out_file.close()


if __name__ == '__main__':

    in_file = open('input.txt', 'r')
    input_str = str(in_file.read())
    in_file.close()


    flag = 0
    if flag:
        build()

    json_file = open('output.json')
    data = json.load(json_file)
    cur = 0
    print('\nRotelectus v0.0.1 prototype\n')
    print('-------------------------------------------------------')
    print('[LOG] Start sentence processing ...')
    equ = -1
    print('[LOG] Printing original sentence: ')
    print(input_str, '\n')
    print('[LOG] Printing tokens: ')
    toks = data['tok'][0]
    print(toks, '\n')
    for i in range(len(toks)):
        tok_c = toks[i]
        if tok_c == '是':
            equ = i
            break
    print('[LOG] Got relation keyword \'是\' at position:', equ)
    json_file.close()
    print('[LOG] All jobs finished and exiting ...')
    print('-------------------------------------------------------\n')
