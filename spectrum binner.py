"""
This script generates then iterates through a mzML file, binning a specified number of spectra
v02
new:
    no longer requires all spectra to be pulled
    bins spectra as each is pulled
    fixed specified scan range trigger for output
    ---02---
    works with _mzML
    specific functions (now in tome) are called instead of *
    ---03---
    removed save spectra function (now in XLSX)
    cleaned up calls
    
    ---4.0---
to add:
    convert to use XLSX class
    fix calls to mzml and tome
    default outname for savemassspectrum (and iterates if a duplicate is found)
    move functions into tome and rewrite to call those
    output for more than one spectrum (MSMS ramping functionality)
"""

def sumspectra(filename,sr='all',excel=None):
    """
    Sums spectra from raw file and outputs to excel file 
    
    input: filename, *kwargs
    filename:
        name of raw file
    sr:
        scan range to sum
        default 'all'
        specify with [start scan,end scan]
    """
    import os,sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/_classes')
    from _mzML import mzML
    from _XLSX import XLSX
    from _ScriptTime import ScriptTime
    
    st = ScriptTime()
    st.printstart()
    mzml = mzML(filename[:-4]+'.mzML') # create mzML object
    summed,sr = mzml.sumscans(sr)
    xlfile = XLSX(filename[:-4],create=True)
    xlfile.writespectrum(summed[0],summed[1],'summed spectra (scans %d-%d)' %(sr[0],sr[1]))
    xlfile.save()
    st.printend()
    
if __name__ == '__main__':
    # raw filename to use
    filename = 'LY-2016-06-13 09.raw'
    
    # scan range to sum (default 'all')
    sr = 'all'
    
    sumspectra(filename,sr=sr)    