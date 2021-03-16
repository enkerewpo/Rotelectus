'''
@author Kvar_ispw17
@email enkerewpo@gmail.com
'''

import hanlp

if __name__ == '__main__':
    HanLP = hanlp.load(hanlp.pretrained.mtl.OPEN_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
    HanLP(['2021年 HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。']).pretty_print()