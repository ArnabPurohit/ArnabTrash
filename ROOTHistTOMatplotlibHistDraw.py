from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1D
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
import matplotlib.pyplot as plt
import numpy as np
import math
bincon = []
binerr = []
ibin = []
hfile = TFile( 'output_data_single_passingIDMVA.root', 'READ', 'Demo ROOT file with histograms' )
hfile.ls()
hist = hfile.Get("bin01_probe_sc_abseta_0p00To1p44_probe_Pho_r9_0p85To1p00_Fail")
for i in range(1,hist.GetNbinsX()):
    print i,
    ibin.append(hist.GetBinCenter(i))
    bincon.append(hist.GetBinContent(i))
    binerr.append(hist.GetBinError(i))
print bincon
print binerr
bar = plt.bar(ibin, bincon, yerr=binerr)
#plt.yticks(np.arange(0,0.35,step=0.05))
#plt.ylabel('Percentage of appearance')
plt.xlabel('Inv. Mass')   
for i, rectangle in enumerate(bar):
    print i
    print bincon[i], " and error ", binerr[i]
    height = rectangle.get_height()
    print height
    plt.text(rectangle.get_x() + rectangle.get_width()/2, height+0.1,
             '$\mu=$%s, $\sigma=$%s, $\sqrt{\mu}=$%s' % (str(round(bincon[i],2)), str(round(binerr[i],2)), str(round(math.sqrt(bincon[i]),2))),
             ha='center', va='bottom',rotation=90)
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,y1,y2*2.))
plt.show()
