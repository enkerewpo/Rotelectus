# -*- coding:utf-8 -*-
# Author: Kvar_ispw17
import hanlp

if __name__ == '__main__':

    # input file opening
    in_file = open('input.txt', 'r')
    input_str = str(in_file.read())

    # output the json file to $output.json
    out_file = open('output.json', 'w')
    HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)
    out_str = str(HanLP([input_str]))

    # pretty print the structure in terminal
    HanLP([input_str]).pretty_print()

    out_file.write(out_str)

    # file closing
    in_file.close()
    out_file.close()
