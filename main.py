# -*- coding:utf-8 -*-
# Author: Kvar_ispw17
import hanlp

if __name__ == '__main__':

    in_file = open('input.txt', 'r')
    input_str = str(in_file.read())

    out_file = open('output.json', 'w')
    HanLP = hanlp.load(hanlp.pretrained.mtl.OPEN_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
    out_str = str(HanLP([input_str]))

    HanLP([input_str]).pretty_print()

    out_file.write(out_str)

    in_file.close()
    out_file.close()
