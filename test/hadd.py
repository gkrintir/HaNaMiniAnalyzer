#!/usr/bin/env python
from ROOT import gROOT
gROOT.SetBatch(True)

from Samples80tHq.Samples import *
samples = None
runOnOutsOfAnotherJob = False
if runOnOutsOfAnotherJob :
    samples = samples24june
    samples += sampleswith24juneonly
else :
    samples = MicroAOD80Samples

for sample in samples:
    #if sample.Name in [s.Name for s in sampleswith24juneonly]:
        #job is already created : sample.MakeJobs( 20 , "%s/%s" % (OutPath24June , prefix) )
    #    print sample.Name 
    #else:
    sample.MakeJobs( 3 , "eos/cms/store/user/%s/%s/%s" % (GetUserName(), "thqTree2016" , "tree" ) ) 

from tHqAnalyzer.HaNaMiniAnalyzer.ExtendedSample import *
for sample in samples:
    if sample.Name in ["DiPhoton_Jets"]:
    #    print "skipping " + sample.Name
    #    continue
        ss = ExtendedSample(sample)
    #export EOS_MGM_URL=root://eosuser.cern.ch
    #eosmount eos_cb
        ss.fhadd("eos_cb/user/h/hbakhshi/Personal/Projects/tHq/nTuples/")
