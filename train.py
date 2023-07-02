from __future__ import absolute_import

import os
from got10k.datasets import *

from siamfc import TrackerSiamFC
from rpn.siamrpn import TrackerSiamRPN

if __name__ == '__main__':
    # root_dir = os.path.expanduser('~/data/GOT-10k')
    # seqs = GOT10k(root_dir, subset='train', return_meta=True)

    root_dir = os.path.expanduser('/kaggle/input/otb2015/OTB100')
    seqs = OTB(root_dir, version=2015)

    # 定义学生模型SiamFC
    student_tracker = TrackerSiamFC()
    # 定义教师模型SiamRPN，加载预训练模型
    teacher_tracker = TrackerSiamRPN(net_path='/home/UserDirectory/gly/code/SiamFC_KD/pretrained/SiamRPN.pth')

    # 训练学生模型,使用teacher_tracker进行蒸馏
    student_tracker.KD_train(seqs, teacher_tracker, save_path='./home/UserDirectory/gly/code/SiamFC_KD/pretrained/student.pth')
    
    
