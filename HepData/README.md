
HepData instructions:

https://indico.cern.ch/event/992125/contributions/4172914/attachments/2171614/3666432/2021-01-14_hepdata_for_wgm.pdf
https://hub.docker.com/r/clelange/hepdata_lib/

in practice, on lxplus:

$ setenv SINGULARITY_CACHEDIR "/tmp/${whoami}/singularity"
$ singularity shell -B /afs -B /eos docker://clelange/hepdata_lib bash
Singularity> python createHepData.py

Then download the submission tar file and upload it here:
https://www.hepdata.net/record/sandbox