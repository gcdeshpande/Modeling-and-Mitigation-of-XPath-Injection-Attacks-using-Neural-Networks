#!/usr/bin/env python
#############################################################################
# Copyright (C) 2013, OpenEye Scientific Software, Inc.
#############################################################################
# Plotting ROC curve
#############################################################################

import sys
import os
from operator import itemgetter
import matplotlib.pyplot as plt


def main(argv=[__name__]):

    if len(sys.argv) != 4:
        print "usage: <actives> <scores>] <image>"
        sys.exit(0)

    afname = sys.argv[1]
    sfname = sys.argv[2]
    ofname = sys.argv[3]

    f, ext = os.path.splitext(ofname)
    if not IsSupportedImageType(ext):
        print("Format \"%s\" is not supported!" % ext)
        sys.exit(0)

    # read id of actives

    actives = LoadActives(afname)
    print("Loaded %d actives from %s" % (len(actives), afname))

    # read molecule id - score pairs

    label, scores = LoadScores(sfname)
    print("Loaded %d %s scores from %s" % (len(scores), label, sfname))

    # sort scores by ascending order
    sortedscores = sorted(scores, key=itemgetter(1))

    print("Plotting ROC Curve ...")
    color = "#008000"  # dark green
    DepictROCCurve(actives, sortedscores, label, color, ofname)


def LoadActives(fname):

    actives = []
    for line in open(fname, 'r').readlines():
        id = line.strip()
        actives.append(id)

    return actives


def LoadScores(fname):

    sfile = open(fname, 'r')
    label = sfile.readline()
    label = label.strip()

    scores = []
    for line in sfile.readlines():
        id, score = line.strip().split()
        scores.append((id, float(score)))

    return label, scores


def GetRates(actives, scores):

    tpr = [0.0]  # true positive rate
    fpr = [0.0]  # false positive rate
    nractives = len(actives)
    nrdecoys = len(scores) - len(actives)

    foundactives = 0.0
    founddecoys = 0.0
    for idx, (id, score) in enumerate(scores):
        if id in actives:
            foundactives += 1.0
        else:
            founddecoys += 1.0

        tpr.append(foundactives / float(nractives))
        fpr.append(founddecoys / float(nrdecoys))

    return tpr, fpr


def SetupROCCurvePlot(plt):

    plt.xlabel("FPR", fontsize=14)
    plt.ylabel("TPR", fontsize=14)
    plt.title("ROC Curve", fontsize=14)


def SaveROCCurvePlot(plt, fname, randomline=True):

    if randomline:
        x = [0.0, 1.0]
        plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.legend(fontsize=10, loc='best')
    plt.tight_layout()
    plt.savefig(fname)


def AddROCCurve(plt, actives, scores, color, label):

    tpr, fpr = GetRates(actives, scores)

    plt.plot(fpr, tpr, color=color, linewidth=2, label=label)


def DepictROCCurve(actives, scores, label, color, fname, randomline=True):

    plt.figure(figsize=(4, 4), dpi=80)

    SetupROCCurvePlot(plt)
    AddROCCurve(plt, actives, scores, color, label)
    SaveROCCurvePlot(plt, fname, randomline)


def IsSupportedImageType(ext):
    fig = plt.figure()
    return (ext[1:] in fig.canvas.get_supported_filetypes())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
