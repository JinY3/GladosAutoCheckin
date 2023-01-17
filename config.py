# -*- coding: UTF-8 -*-
import os
#cookie中的koa:sess与koa:sess.sig参数
KOA_SESS = os.environ['KOA_SESS'].strip()
KOA_SESS_SIG = os.environ['KOA_SESS_SIG'].strip()
SCKEY = os.environ['SCKEY'].strip()
