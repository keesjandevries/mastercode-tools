import getpass
import socket

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def base_directory() :
    return  "/vols/cms04/kjd110/multinest_output/"

def iter_directory() :
    return  "/vols/cms04/kjd110/multinest_cmssm-1000-live-10-step-200-iter/"

def nuhm2_boxes_directory():
    return "/vols/cms04/kjd110/nuhm2_sampling"

def nuhm2_xmas_directory():
    return "/vols/cms04/kjd110/nuhm2_xmas"

def nuhm2_ndn_directory():
    return "/vols/cms04/kjd110/nuhm2_ndn_boxes"

def boxes_directory():
#  return "/vols/cms04/kjd110/small_mn_parallel/"
    return "/vols/cms04/kjd110/mn_parallel/"

def boxes_N_directory(n):
    dir = ("/vols/cms04/kjd110/mn_parallel_%i/" % n)
    return dir

def nuhm2_ndn_sub_dirs(i):
    l=["1700_0_0_2_0_0_4000_2000_5000_68_10M_10M_",
"1700_0_0_2_0_0_4000_4000_5000_35_10M_10M_",
"1700_0_0_2_0_-10M_4000_2000_5000_35_10M_10M_",
"1700_0_0_2_0_-10M_4000_2000_5000_68_10M_0_",
"1700_0_0_2_0_-10M_4000_4000_5000_35_10M_0_",
"1700_0_0_2_-10M_0_4000_2000_5000_35_10M_10M_",
"1700_0_0_2_-10M_0_4000_2000_5000_68_0_10M_",
"1700_0_0_2_-10M_0_4000_4000_5000_35_0_10M_",
"1700_0_0_2_-10M_-10M_4000_2000_5000_35_0_10M_",
"1700_0_0_2_-10M_-10M_4000_2000_5000_35_10M_0_",
"1700_0_0_2_-10M_-10M_4000_2000_5000_68_0_0_",
"1700_0_0_2_-10M_-10M_4000_4000_5000_35_0_0_",
"1700_0_0_35_0_0_4000_4000_5000_68_10M_10M_",
"1700_0_0_35_0_-10M_4000_2000_5000_68_10M_10M_",
"1700_0_0_35_0_-10M_4000_4000_5000_68_10M_0_",
"1700_0_0_35_-10M_0_4000_2000_5000_68_10M_10M_",
"1700_0_0_35_-10M_0_4000_4000_5000_68_0_10M_",
"1700_0_0_35_-10M_-10M_4000_2000_5000_68_0_10M_",
"1700_0_0_35_-10M_-10M_4000_2000_5000_68_10M_0_",
"1700_0_0_35_-10M_-10M_4000_4000_5000_68_0_0_",
"1700_0_-5000_2_0_0_4000_2000_0_68_10M_10M_",
"1700_0_-5000_2_0_0_4000_2000_5000_35_10M_10M_",
"1700_0_-5000_2_0_0_4000_4000_0_35_10M_10M_",
"1700_0_-5000_2_0_-10M_4000_2000_0_35_10M_10M_",
"1700_0_-5000_2_0_-10M_4000_2000_0_68_10M_0_",
"1700_0_-5000_2_0_-10M_4000_2000_5000_35_10M_0_",
"1700_0_-5000_2_0_-10M_4000_4000_0_35_10M_0_",
"1700_0_-5000_2_-10M_0_4000_2000_0_35_10M_10M_",
"1700_0_-5000_2_-10M_0_4000_2000_0_68_0_10M_",
"1700_0_-5000_2_-10M_0_4000_2000_5000_35_0_10M_",
"1700_0_-5000_2_-10M_0_4000_4000_0_35_0_10M_",
"1700_0_-5000_2_-10M_-10M_4000_2000_0_35_0_10M_",
"1700_0_-5000_2_-10M_-10M_4000_2000_0_35_10M_0_",
"1700_0_-5000_2_-10M_-10M_4000_2000_0_68_0_0_",
"1700_0_-5000_2_-10M_-10M_4000_2000_5000_35_0_0_",
"1700_0_-5000_2_-10M_-10M_4000_4000_0_35_0_0_",
"1700_0_-5000_35_0_0_4000_2000_5000_68_10M_10M_",
"1700_0_-5000_35_0_0_4000_4000_0_68_10M_10M_",
"1700_0_-5000_35_0_-10M_4000_2000_0_68_10M_10M_",
"1700_0_-5000_35_0_-10M_4000_2000_5000_68_10M_0_",
"1700_0_-5000_35_0_-10M_4000_4000_0_68_10M_0_",
"1700_0_-5000_35_-10M_0_4000_2000_0_68_10M_10M_",
"1700_0_-5000_35_-10M_0_4000_2000_5000_68_0_10M_",
"1700_0_-5000_35_-10M_0_4000_4000_0_68_0_10M_",
"1700_0_-5000_35_-10M_-10M_4000_2000_0_68_0_10M_",
"1700_0_-5000_35_-10M_-10M_4000_2000_0_68_10M_0_",
"1700_0_-5000_35_-10M_-10M_4000_2000_5000_68_0_0_",
"1700_0_-5000_35_-10M_-10M_4000_4000_0_68_0_0_",
"1700_2000_0_2_0_0_4000_4000_5000_68_10M_10M_",
"1700_2000_0_2_0_-10M_4000_4000_5000_35_10M_10M_",
"1700_2000_0_2_0_-10M_4000_4000_5000_68_10M_0_",
"1700_2000_0_2_-10M_0_4000_4000_5000_35_10M_10M_",
"1700_2000_0_2_-10M_0_4000_4000_5000_68_0_10M_",
"1700_2000_0_2_-10M_-10M_4000_4000_5000_35_0_10M_",
"1700_2000_0_2_-10M_-10M_4000_4000_5000_35_10M_0_",
"1700_2000_0_2_-10M_-10M_4000_4000_5000_68_0_0_",
"1700_2000_0_35_0_-10M_4000_4000_5000_68_10M_10M_",
"1700_2000_0_35_-10M_0_4000_4000_5000_68_10M_10M_",
"1700_2000_0_35_-10M_-10M_4000_4000_5000_68_0_10M_",
"1700_2000_0_35_-10M_-10M_4000_4000_5000_68_10M_0_",
"1700_2000_-5000_2_0_0_4000_4000_0_68_10M_10M_",
"1700_2000_-5000_2_0_0_4000_4000_5000_35_10M_10M_",
"1700_2000_-5000_2_0_-10M_4000_4000_0_35_10M_10M_",
"1700_2000_-5000_2_0_-10M_4000_4000_0_68_10M_0_",
"1700_2000_-5000_2_0_-10M_4000_4000_5000_35_10M_0_",
"1700_2000_-5000_2_-10M_0_4000_4000_0_35_10M_10M_",
"1700_2000_-5000_2_-10M_0_4000_4000_0_68_0_10M_",
"1700_2000_-5000_2_-10M_0_4000_4000_5000_35_0_10M_",
"1700_2000_-5000_2_-10M_-10M_4000_4000_0_35_0_10M_",
"1700_2000_-5000_2_-10M_-10M_4000_4000_0_35_10M_0_",
"1700_2000_-5000_2_-10M_-10M_4000_4000_0_68_0_0_",
"1700_2000_-5000_2_-10M_-10M_4000_4000_5000_35_0_0_",
"1700_2000_-5000_35_0_0_4000_4000_5000_68_10M_10M_",
"1700_2000_-5000_35_0_-10M_4000_4000_0_68_10M_10M_",
"1700_2000_-5000_35_0_-10M_4000_4000_5000_68_10M_0_",
"1700_2000_-5000_35_-10M_0_4000_4000_0_68_10M_10M_",
"1700_2000_-5000_35_-10M_0_4000_4000_5000_68_0_10M_",
"1700_2000_-5000_35_-10M_-10M_4000_4000_0_68_0_10M_",
"1700_2000_-5000_35_-10M_-10M_4000_4000_0_68_10M_0_",
"1700_2000_-5000_35_-10M_-10M_4000_4000_5000_68_0_0_",
"-600_0_0_2_0_0_1700_2000_5000_68_10M_10M_",
"-600_0_0_2_0_0_1700_4000_5000_35_10M_10M_",
"-600_0_0_2_0_0_4000_2000_5000_35_10M_10M_",
"-600_0_0_2_0_-10M_1700_2000_5000_35_10M_10M_",
"-600_0_0_2_0_-10M_1700_2000_5000_68_10M_0_",
"-600_0_0_2_0_-10M_1700_4000_5000_35_10M_0_",
"-600_0_0_2_0_-10M_4000_2000_5000_35_10M_0_",
"-600_0_0_2_-10M_0_1700_2000_5000_35_10M_10M_",
"-600_0_0_2_-10M_0_1700_2000_5000_68_0_10M_",
"-600_0_0_2_-10M_0_1700_4000_5000_35_0_10M_",
"-600_0_0_2_-10M_0_4000_2000_5000_35_0_10M_",
"-600_0_0_2_-10M_-10M_1700_2000_5000_35_0_10M_",
"-600_0_0_2_-10M_-10M_1700_2000_5000_35_10M_0_",
"-600_0_0_2_-10M_-10M_1700_2000_5000_68_0_0_",
"-600_0_0_2_-10M_-10M_1700_4000_5000_35_0_0_",
"-600_0_0_2_-10M_-10M_4000_2000_5000_35_0_0_",
"-600_0_0_35_0_0_1700_4000_5000_68_10M_10M_",
"-600_0_0_35_0_0_4000_2000_5000_68_10M_10M_",
"-600_0_0_35_0_-10M_1700_2000_5000_68_10M_10M_",
"-600_0_0_35_0_-10M_1700_4000_5000_68_10M_0_",
"-600_0_0_35_0_-10M_4000_2000_5000_68_10M_0_",
"-600_0_0_35_-10M_0_1700_2000_5000_68_10M_10M_",
"-600_0_0_35_-10M_0_1700_4000_5000_68_0_10M_",
"-600_0_0_35_-10M_0_4000_2000_5000_68_0_10M_",
"-600_0_0_35_-10M_-10M_1700_2000_5000_68_0_10M_",
"-600_0_0_35_-10M_-10M_1700_2000_5000_68_10M_0_",
"-600_0_0_35_-10M_-10M_1700_4000_5000_68_0_0_",
"-600_0_0_35_-10M_-10M_4000_2000_5000_68_0_0_",
"-600_0_-5000_2_0_0_1700_2000_0_68_10M_10M_",
"-600_0_-5000_2_0_0_1700_2000_5000_35_10M_10M_",
"-600_0_-5000_2_0_0_1700_4000_0_35_10M_10M_",
"-600_0_-5000_2_0_0_4000_2000_0_35_10M_10M_",
"-600_0_-5000_2_0_-10M_1700_2000_0_35_10M_10M_",
"-600_0_-5000_2_0_-10M_1700_2000_0_68_10M_0_",
"-600_0_-5000_2_0_-10M_1700_2000_5000_35_10M_0_",
"-600_0_-5000_2_0_-10M_1700_4000_0_35_10M_0_",
"-600_0_-5000_2_0_-10M_4000_2000_0_35_10M_0_",
"-600_0_-5000_2_-10M_0_1700_2000_0_35_10M_10M_",
"-600_0_-5000_2_-10M_0_1700_2000_0_68_0_10M_",
"-600_0_-5000_2_-10M_0_1700_2000_5000_35_0_10M_",
"-600_0_-5000_2_-10M_0_1700_4000_0_35_0_10M_",
"-600_0_-5000_2_-10M_0_4000_2000_0_35_0_10M_",
"-600_0_-5000_2_-10M_-10M_1700_2000_0_35_0_10M_",
"-600_0_-5000_2_-10M_-10M_1700_2000_0_35_10M_0_",
"-600_0_-5000_2_-10M_-10M_1700_2000_0_68_0_0_",
"-600_0_-5000_2_-10M_-10M_1700_2000_5000_35_0_0_",
"-600_0_-5000_2_-10M_-10M_1700_4000_0_35_0_0_",
"-600_0_-5000_2_-10M_-10M_4000_2000_0_35_0_0_",
"-600_0_-5000_35_0_0_1700_2000_5000_68_10M_10M_",
"-600_0_-5000_35_0_0_1700_4000_0_68_10M_10M_",
"-600_0_-5000_35_0_0_4000_2000_0_68_10M_10M_",
"-600_0_-5000_35_0_-10M_1700_2000_0_68_10M_10M_",
"-600_0_-5000_35_0_-10M_1700_2000_5000_68_10M_0_",
"-600_0_-5000_35_0_-10M_1700_4000_0_68_10M_0_",
"-600_0_-5000_35_0_-10M_4000_2000_0_68_10M_0_",
"-600_0_-5000_35_-10M_0_1700_2000_0_68_10M_10M_",
"-600_0_-5000_35_-10M_0_1700_2000_5000_68_0_10M_",
"-600_0_-5000_35_-10M_0_1700_4000_0_68_0_10M_",
"-600_0_-5000_35_-10M_0_4000_2000_0_68_0_10M_",
"-600_0_-5000_35_-10M_-10M_1700_2000_0_68_0_10M_",
"-600_0_-5000_35_-10M_-10M_1700_2000_0_68_10M_0_",
"-600_0_-5000_35_-10M_-10M_1700_2000_5000_68_0_0_",
"-600_0_-5000_35_-10M_-10M_1700_4000_0_68_0_0_",
"-600_0_-5000_35_-10M_-10M_4000_2000_0_68_0_0_",
"-600_2000_0_2_0_0_1700_4000_5000_68_10M_10M_",
"-600_2000_0_2_0_0_4000_4000_5000_35_10M_10M_",
"-600_2000_0_2_0_-10M_1700_4000_5000_35_10M_10M_",
"-600_2000_0_2_0_-10M_1700_4000_5000_68_10M_0_",
"-600_2000_0_2_0_-10M_4000_4000_5000_35_10M_0_",
"-600_2000_0_2_-10M_0_1700_4000_5000_35_10M_10M_",
"-600_2000_0_2_-10M_0_1700_4000_5000_68_0_10M_",
"-600_2000_0_2_-10M_0_4000_4000_5000_35_0_10M_",
"-600_2000_0_2_-10M_-10M_1700_4000_5000_35_0_10M_",
"-600_2000_0_2_-10M_-10M_1700_4000_5000_35_10M_0_",
"-600_2000_0_2_-10M_-10M_1700_4000_5000_68_0_0_",
"-600_2000_0_2_-10M_-10M_4000_4000_5000_35_0_0_",
"-600_2000_0_35_0_0_4000_4000_5000_68_10M_10M_",
"-600_2000_0_35_0_-10M_1700_4000_5000_68_10M_10M_",
"-600_2000_0_35_0_-10M_4000_4000_5000_68_10M_0_",
"-600_2000_0_35_-10M_0_1700_4000_5000_68_10M_10M_",
"-600_2000_0_35_-10M_0_4000_4000_5000_68_0_10M_",
"-600_2000_0_35_-10M_-10M_1700_4000_5000_68_0_10M_",
"-600_2000_0_35_-10M_-10M_1700_4000_5000_68_10M_0_",
"-600_2000_0_35_-10M_-10M_4000_4000_5000_68_0_0_",
"-600_2000_-5000_2_0_0_1700_4000_0_68_10M_10M_",
"-600_2000_-5000_2_0_0_1700_4000_5000_35_10M_10M_",
"-600_2000_-5000_2_0_0_4000_4000_0_35_10M_10M_",
"-600_2000_-5000_2_0_-10M_1700_4000_0_35_10M_10M_",
"-600_2000_-5000_2_0_-10M_1700_4000_0_68_10M_0_",
"-600_2000_-5000_2_0_-10M_1700_4000_5000_35_10M_0_",
"-600_2000_-5000_2_0_-10M_4000_4000_0_35_10M_0_",
"-600_2000_-5000_2_-10M_0_1700_4000_0_35_10M_10M_",
"-600_2000_-5000_2_-10M_0_1700_4000_0_68_0_10M_",
"-600_2000_-5000_2_-10M_0_1700_4000_5000_35_0_10M_",
"-600_2000_-5000_2_-10M_0_4000_4000_0_35_0_10M_",
"-600_2000_-5000_2_-10M_-10M_1700_4000_0_35_0_10M_",
"-600_2000_-5000_2_-10M_-10M_1700_4000_0_35_10M_0_",
"-600_2000_-5000_2_-10M_-10M_1700_4000_0_68_0_0_",
"-600_2000_-5000_2_-10M_-10M_1700_4000_5000_35_0_0_",
"-600_2000_-5000_2_-10M_-10M_4000_4000_0_35_0_0_",
"-600_2000_-5000_35_0_0_1700_4000_5000_68_10M_10M_",
"-600_2000_-5000_35_0_0_4000_4000_0_68_10M_10M_",
"-600_2000_-5000_35_0_-10M_1700_4000_0_68_10M_10M_",
"-600_2000_-5000_35_0_-10M_1700_4000_5000_68_10M_0_",
"-600_2000_-5000_35_0_-10M_4000_4000_0_68_10M_0_",
"-600_2000_-5000_35_-10M_0_1700_4000_0_68_10M_10M_",
"-600_2000_-5000_35_-10M_0_1700_4000_5000_68_0_10M_",
"-600_2000_-5000_35_-10M_0_4000_4000_0_68_0_10M_",
"-600_2000_-5000_35_-10M_-10M_1700_4000_0_68_0_10M_",
"-600_2000_-5000_35_-10M_-10M_1700_4000_0_68_10M_0_",
"-600_2000_-5000_35_-10M_-10M_1700_4000_5000_68_0_0_",
"-600_2000_-5000_35_-10M_-10M_4000_4000_0_68_0_0_",]
    return l[i]

def nuhm2_xmas_sub_dirs(i):
    l=[
"1800_0_0_2_0_0_4000_2000_5000_35_10M_10M_",
"1800_0_0_2_0_-10M_4000_2000_5000_35_10M_0_",
"1800_0_0_2_-10M_0_4000_2000_5000_35_0_10M_",
"1800_0_0_2_-10M_-10M_4000_2000_5000_35_0_0_",
"1800_0_0_35_0_0_4000_2000_5000_68_10M_10M_",
"1800_0_0_35_0_-10M_4000_2000_5000_68_10M_0_",
"1800_0_0_35_-10M_0_4000_2000_5000_68_0_10M_",
"1800_0_0_35_-10M_-10M_4000_2000_5000_68_0_0_",
"1800_0_-5000_2_0_0_4000_2000_0_35_10M_10M_",
"1800_0_-5000_2_0_-10M_4000_2000_0_35_10M_0_",
"1800_0_-5000_2_-10M_0_4000_2000_0_35_0_10M_",
"1800_0_-5000_2_-10M_-10M_4000_2000_0_35_0_0_",
"1800_0_-5000_35_0_0_4000_2000_0_68_10M_10M_",
"1800_0_-5000_35_0_-10M_4000_2000_0_68_10M_0_",
"1800_0_-5000_35_-10M_0_4000_2000_0_68_0_10M_",
"1800_0_-5000_35_-10M_-10M_4000_2000_0_68_0_0_",
"1800_2000_0_2_0_0_4000_4000_5000_35_10M_10M_",
"1800_2000_0_2_0_-10M_4000_4000_5000_35_10M_0_",
"1800_2000_0_2_-10M_0_4000_4000_5000_35_0_10M_",
"1800_2000_0_2_-10M_-10M_4000_4000_5000_35_0_0_",
"1800_2000_0_35_0_0_4000_4000_5000_68_10M_10M_",
"1800_2000_0_35_0_-10M_4000_4000_5000_68_10M_0_",
"1800_2000_0_35_-10M_0_4000_4000_5000_68_0_10M_",
"1800_2000_0_35_-10M_-10M_4000_4000_5000_68_0_0_",
"1800_2000_-5000_2_0_0_4000_4000_0_35_10M_10M_",
"1800_2000_-5000_2_0_-10M_4000_4000_0_35_10M_0_",
"1800_2000_-5000_2_-10M_0_4000_4000_0_35_0_10M_",
"1800_2000_-5000_2_-10M_-10M_4000_4000_0_35_0_0_",
"1800_2000_-5000_35_0_0_4000_4000_0_68_10M_10M_",
"1800_2000_-5000_35_0_-10M_4000_4000_0_68_10M_0_",
"1800_2000_-5000_35_-10M_0_4000_4000_0_68_0_10M_",
"1800_2000_-5000_35_-10M_-10M_4000_4000_0_68_0_0_",
"-400_0_0_2_0_0_1800_2000_5000_35_10M_10M_",
"-400_0_0_2_0_-10M_1800_2000_5000_35_10M_0_",
"-400_0_0_2_-10M_0_1800_2000_5000_35_0_10M_",
"-400_0_0_2_-10M_-10M_1800_2000_5000_35_0_0_",
"-400_0_0_35_0_0_1800_2000_5000_68_10M_10M_",
"-400_0_0_35_0_-10M_1800_2000_5000_68_10M_0_",
"-400_0_0_35_-10M_0_1800_2000_5000_68_0_10M_",
"-400_0_0_35_-10M_-10M_1800_2000_5000_68_0_0_",
"-400_0_-5000_2_0_0_1800_2000_0_35_10M_10M_",
"-400_0_-5000_2_0_-10M_1800_2000_0_35_10M_0_",
"-400_0_-5000_2_-10M_0_1800_2000_0_35_0_10M_",
"-400_0_-5000_2_-10M_-10M_1800_2000_0_35_0_0_",
"-400_0_-5000_35_0_0_1800_2000_0_68_10M_10M_",
"-400_0_-5000_35_0_-10M_1800_2000_0_68_10M_0_",
"-400_0_-5000_35_-10M_0_1800_2000_0_68_0_10M_",
"-400_0_-5000_35_-10M_-10M_1800_2000_0_68_0_0_",
"-400_2000_0_2_0_0_1800_4000_5000_35_10M_10M_",
"-400_2000_0_2_0_-10M_1800_4000_5000_35_10M_0_",
"-400_2000_0_2_-10M_0_1800_4000_5000_35_0_10M_",
"-400_2000_0_2_-10M_-10M_1800_4000_5000_35_0_0_",
"-400_2000_0_35_0_0_1800_4000_5000_68_10M_10M_",
"-400_2000_0_35_0_-10M_1800_4000_5000_68_10M_0_",
"-400_2000_0_35_-10M_0_1800_4000_5000_68_0_10M_",
"-400_2000_0_35_-10M_-10M_1800_4000_5000_68_0_0_",
"-400_2000_-5000_2_0_0_1800_4000_0_35_10M_10M_",
"-400_2000_-5000_2_0_-10M_1800_4000_0_35_10M_0_",
"-400_2000_-5000_2_-10M_0_1800_4000_0_35_0_10M_",
"-400_2000_-5000_2_-10M_-10M_1800_4000_0_35_0_0_",
"-400_2000_-5000_35_0_0_1800_4000_0_68_10M_10M_",
"-400_2000_-5000_35_0_-10M_1800_4000_0_68_10M_0_",
"-400_2000_-5000_35_-10M_0_1800_4000_0_68_0_10M_",
"-400_2000_-5000_35_-10M_-10M_1800_4000_0_68_0_0_",]
    return l[i]

def cmssm_boxes_sub_dirs(i):
    l=[    
"0_0_1666_2_1333_1333_4999_24",
"0_0_1666_24_1333_1333_4999_46",
"0_0_1666_46_1333_1333_4999_68",
"0_0_-1667_2_1333_1333_1666_24",
"0_0_-1667_24_1333_1333_1666_46",
"0_0_-1667_46_1333_1333_1666_68",
"0_0_-5000_2_1333_1333_-1667_24",
"0_0_-5000_24_1333_1333_-1667_46",
"0_0_-5000_46_1333_1333_-1667_68",
"0_1333_1666_2_1333_2666_4999_24",
"0_1333_1666_24_1333_2666_4999_46",
"0_1333_1666_46_1333_2666_4999_68",
"0_1333_-1667_2_1333_2666_1666_24",
"0_1333_-1667_24_1333_2666_1666_46",
"0_1333_-1667_46_1333_2666_1666_68",
"0_1333_-5000_2_1333_2666_-1667_24",
"0_1333_-5000_24_1333_2666_-1667_46",
"0_1333_-5000_46_1333_2666_-1667_68",
"0_2666_1666_2_1333_3999_4999_24",
"0_2666_1666_24_1333_3999_4999_46",
"0_2666_1666_46_1333_3999_4999_68",
"0_2666_-1667_2_1333_3999_1666_24",
"0_2666_-1667_24_1333_3999_1666_46",
"0_2666_-1667_46_1333_3999_1666_68",
"0_2666_-5000_2_1333_3999_-1667_24",
"0_2666_-5000_24_1333_3999_-1667_46",
"0_2666_-5000_46_1333_3999_-1667_68",
"1333_0_1666_2_2666_1333_4999_24",
"1333_0_1666_24_2666_1333_4999_46",
"1333_0_1666_46_2666_1333_4999_68",
"1333_0_-1667_2_2666_1333_1666_24",
"1333_0_-1667_24_2666_1333_1666_46",
"1333_0_-1667_46_2666_1333_1666_68",
"1333_0_-5000_2_2666_1333_-1667_24",
"1333_0_-5000_24_2666_1333_-1667_46",
"1333_0_-5000_46_2666_1333_-1667_68",
"1333_1333_1666_2_2666_2666_4999_24",
"1333_1333_1666_24_2666_2666_4999_46",
"1333_1333_1666_46_2666_2666_4999_68",
"1333_1333_-1667_2_2666_2666_1666_24",
"1333_1333_-1667_24_2666_2666_1666_46",
"1333_1333_-1667_46_2666_2666_1666_68",
"1333_1333_-5000_2_2666_2666_-1667_24",
"1333_1333_-5000_24_2666_2666_-1667_46",
"1333_1333_-5000_46_2666_2666_-1667_68",
"1333_2666_1666_2_2666_3999_4999_24",
"1333_2666_1666_24_2666_3999_4999_46",
"1333_2666_1666_46_2666_3999_4999_68",
"1333_2666_-1667_2_2666_3999_1666_24",
"1333_2666_-1667_24_2666_3999_1666_46",
"1333_2666_-1667_46_2666_3999_1666_68",
"1333_2666_-5000_2_2666_3999_-1667_24",
"1333_2666_-5000_24_2666_3999_-1667_46",
"1333_2666_-5000_46_2666_3999_-1667_68",
"2666_0_1666_2_3999_1333_4999_24",
"2666_0_1666_24_3999_1333_4999_46",
"2666_0_1666_46_3999_1333_4999_68",
"2666_0_-1667_2_3999_1333_1666_24",
"2666_0_-1667_24_3999_1333_1666_46",
"2666_0_-1667_46_3999_1333_1666_68",
"2666_0_-5000_2_3999_1333_-1667_24",
"2666_0_-5000_24_3999_1333_-1667_46",
"2666_0_-5000_46_3999_1333_-1667_68",
"2666_1333_1666_2_3999_2666_4999_24",
"2666_1333_1666_24_3999_2666_4999_46",
"2666_1333_1666_46_3999_2666_4999_68",
"2666_1333_-1667_2_3999_2666_1666_24",
"2666_1333_-1667_24_3999_2666_1666_46",
"2666_1333_-1667_46_3999_2666_1666_68",
"2666_1333_-5000_2_3999_2666_-1667_24",
"2666_1333_-5000_24_3999_2666_-1667_46",
"2666_1333_-5000_46_3999_2666_-1667_68",
"2666_2666_1666_2_3999_3999_4999_24",
"2666_2666_1666_24_3999_3999_4999_46",
"2666_2666_1666_46_3999_3999_4999_68",
"2666_2666_-1667_2_3999_3999_1666_24",
"2666_2666_-1667_24_3999_3999_1666_46",
"2666_2666_-1667_46_3999_3999_1666_68",
"2666_2666_-5000_2_3999_3999_-1667_24",
"2666_2666_-5000_24_3999_3999_-1667_46",
"2666_2666_-5000_46_3999_3999_-1667_68",
]
    return l[i]



def cmssm_boxes_N_sub_dirs(i):
    l=[    
"0_0_1666_2_1333_1333_4999_24",
"0_0_1666_24_1333_1333_4999_46",
"0_0_1666_46_1333_1333_4999_68",
"0_0_-1667_2_1333_1333_1666_24",
"0_0_-1667_24_1333_1333_1666_46",
"0_0_-1667_46_1333_1333_1666_68",
"0_0_-5000_2_1333_1333_-1667_24",
"0_0_-5000_24_1333_1333_-1667_46",
"0_0_-5000_46_1333_1333_-1667_68",
"0_1333_1666_24_1333_2666_4999_46",
"0_1333_1666_46_1333_2666_4999_68",
"0_1333_-1667_24_1333_2666_1666_46",
"0_1333_-1667_46_1333_2666_1666_68",
"0_1333_-5000_24_1333_2666_-1667_46",
"0_1333_-5000_46_1333_2666_-1667_68",
"1333_0_1666_2_2666_1333_4999_24",
"1333_0_1666_24_2666_1333_4999_46",
"1333_0_1666_46_2666_1333_4999_68",
"1333_0_-1667_2_2666_1333_1666_24",
"1333_0_-1667_24_2666_1333_1666_46",
"1333_0_-1667_46_2666_1333_1666_68",
"1333_0_-5000_2_2666_1333_-1667_24",
"1333_0_-5000_24_2666_1333_-1667_46",
"1333_0_-5000_46_2666_1333_-1667_68",
"1333_1333_1666_24_2666_2666_4999_46",
"1333_1333_1666_46_2666_2666_4999_68",
"1333_1333_-1667_46_2666_2666_1666_68",
"1333_1333_-5000_24_2666_2666_-1667_46",
"1333_1333_-5000_46_2666_2666_-1667_68",
"2666_0_1666_2_3999_1333_4999_24",
"2666_0_1666_24_3999_1333_4999_46",
"2666_0_1666_46_3999_1333_4999_68",
"2666_0_-1667_2_3999_1333_1666_24",
"2666_0_-1667_24_3999_1333_1666_46",
"2666_0_-1667_46_3999_1333_1666_68",
"2666_0_-5000_2_3999_1333_-1667_24",
"2666_0_-5000_24_3999_1333_-1667_46",
"2666_0_-5000_46_3999_1333_-1667_68",
"2666_1333_1666_24_3999_2666_4999_46",
"2666_1333_1666_46_3999_2666_4999_68",
"2666_1333_-1667_24_3999_2666_1666_46",
"2666_1333_-1667_46_3999_2666_1666_68",
"2666_1333_-5000_46_3999_2666_-1667_68",]
    return l[i]

def nuhm2_boxes_sub_dirs(i):
    l= [
"_0_0_0_2_0_0_2000_2000_5000_68_10M_10M",
"_0_0_0_2_0_-10M_2000_2000_5000_68_10M_0",
"_0_0_0_2_-10M_0_2000_2000_5000_68_0_10M",
"_0_0_0_2_-10M_-10M_2000_2000_5000_68_0_0",
"_0_0_-5000_2_0_0_2000_2000_0_68_10M_10M",
"_0_0_-5000_2_0_-10M_2000_2000_0_68_10M_0",
"_0_0_-5000_2_-10M_0_2000_2000_0_68_0_10M",
"_0_0_-5000_2_-10M_-10M_2000_2000_0_68_0_0",
"_0_2000_0_2_0_0_2000_4000_5000_68_10M_10M",
"_0_2000_0_2_0_-10M_2000_4000_5000_68_10M_0",
"_0_2000_0_2_-10M_0_2000_4000_5000_68_0_10M",
"_0_2000_0_2_-10M_-10M_2000_4000_5000_68_0_0",
"_0_2000_-5000_2_0_0_2000_4000_0_68_10M_10M",
"_0_2000_-5000_2_0_-10M_2000_4000_0_68_10M_0",
"_0_2000_-5000_2_-10M_0_2000_4000_0_68_0_10M",
"_0_2000_-5000_2_-10M_-10M_2000_4000_0_68_0_0",
"_2000_0_0_2_0_0_4000_2000_5000_68_10M_10M",
"_2000_0_0_2_0_-10M_4000_2000_5000_68_10M_0",
"_2000_0_0_2_-10M_0_4000_2000_5000_68_0_10M",
"_2000_0_0_2_-10M_-10M_4000_2000_5000_68_0_0",
"_2000_0_-5000_2_0_0_4000_2000_0_68_10M_10M",
"_2000_0_-5000_2_0_-10M_4000_2000_0_68_10M_0",
"_2000_0_-5000_2_-10M_0_4000_2000_0_68_0_10M",
"_2000_0_-5000_2_-10M_-10M_4000_2000_0_68_0_0",
"_2000_2000_0_2_0_0_4000_4000_5000_68_10M_10M",
"_2000_2000_0_2_0_-10M_4000_4000_5000_68_10M_0",
"_2000_2000_0_2_-10M_0_4000_4000_5000_68_0_10M",
"_2000_2000_0_2_-10M_-10M_4000_4000_5000_68_0_0",
"_2000_2000_-5000_2_0_0_4000_4000_0_68_10M_10M",
"_2000_2000_-5000_2_0_-10M_4000_4000_0_68_10M_0",
"_2000_2000_-5000_2_-10M_0_4000_4000_0_68_0_10M",
"_2000_2000_-5000_2_-10M_-10M_4000_4000_0_68_0_0",]
    return l[i]

##########################################################################################

def standard_names():
    return{
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
                    }


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

def cmssm_multinest_first_input() :
    # output / global options
    gd = cmssm_multinest_first_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    fd = {
             "FileName"          : "%s/cmssm-10000-iterations-1000-points.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_multinest_first_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_multinest_first.root" % base_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_first_histo() :
    return [MCFile(cmssm_multinest_first_histo_dict() )]


##########################################################################################

def cmssm_multinest_iters_input( iters) :
    # output / global options
    gd = cmssm_multinest_iters_histo_dict(iters)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for iter in range(1,iters+1):
        fd = {
                 "FileName"          : "%s/cmssm-1000-live-%i-step-200-iter.root" % (iter_directory(),iter) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_multinest_iters_histo_dict( iters) :
    d= {
        "FileName"          : "%s/cmssm_multinest_%i_iters.root" % (iter_directory(),iters),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_iters_histo(iters) :
    return [MCFile(cmssm_multinest_iters_histo_dict(iters) )]

def cmssm_multinest_all_iters_histo_list() :
    return [MCFile(cmssm_multinest_iters_histo_dict(iter) ) for iter in range(1,11)]


##########################################################################################

def cmssm_mn_boxes_input(box_n ) :
    # output / global options
    gd = cmssm_mn_boxes_histo_dict(box_n)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(1,11):
        fd = {
                 "FileName"          : "%s/%s/cmssm-step-%i.root" % (boxes_directory(),cmssm_boxes_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_histo_dict( box_n) :
    d= {
        "FileName"          : "%s/%s/cmssm_all.root" % (boxes_directory(), cmssm_boxes_sub_dirs(box_n) ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_histo(box_n) :
    return [MCFile(cmssm_mn_boxes_histo_dict(box_n) )]

def cmssm_mn_boxes_histo_range(range_begin, range_end) :
    return [MCFile(cmssm_mn_boxes_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def cmssm_mn_boxes_N_input(box_n,N ) :
    # output / global options
    gd = cmssm_mn_boxes_N_histo_dict(box_n,N)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(11,41):
        fd = {
                 "FileName"          : "%s/%s/cmssm-step-%i.root" % (boxes_N_directory(N),cmssm_boxes_N_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_N_histo_dict( box_n,N) :
    d= {
        "FileName"          : "%s/%s/cmssm_all.root" % (boxes_N_directory(N), cmssm_boxes_N_sub_dirs(box_n) ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_N_histo(box_n) :
    return [MCFile(cmssm_mn_boxes_N_histo_dict(box_n) )]

def cmssm_mn_boxes_N_histo_range(range_begin, range_end) :
    return [MCFile(cmssm_mn_boxes_N_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def cmssm_mn_boxes_combined_input( ) :
    # output / global options
    gd = cmssm_mn_boxes_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,81):
        fd = {
                 "FileName"          : "%s/%s/cmssm_all.root" % (boxes_directory(), cmssm_boxes_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_combined_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_all_boxes_combined.root" % (boxes_directory(),  ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_combined_histo() :
    return [MCFile(cmssm_mn_boxes_combined_histo_dict() )]


##########################################################################################

def cmssm_mn_boxes_N_combined_input(N ) :
    # output / global options
    gd = cmssm_mn_boxes_N_combined_histo_dict(N)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,43):
        fd = {
                 "FileName"          : "%s/%s/cmssm_all.root" % (boxes_N_directory(N), cmssm_boxes_N_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_N_combined_histo_dict(N) :
    d= {
        "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % (boxes_N_directory(N),  ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_N_combined_histo(N) :
    return [MCFile(cmssm_mn_boxes_N_combined_histo_dict(N) )]


##########################################################################################

def cmssm_multinest_all_sessions_comb_input() :
    # output / global options
    gd = cmssm_multinest_all_sessions_comb_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    fd = {
             "FileName"          : "%s/cmssm_all_boxes_combined.root" % boxes_directory(),
             "Chi2TreeName"      : "tree",
         }
    fd1= {
             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(1),
             "Chi2TreeName"      : "tree",
         }
    fd2= {
             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(2),
             "Chi2TreeName"      : "tree",
         }
#    fd3= {
#             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(3),
#             "Chi2TreeName"      : "tree",
#         }
#    mcfs = [MCFile( fdict, warn = False ) in [fd, fd1 ,fd2,fd3 ]] 
    mcfs = [MCFile( fdict, warn = False ) for fdict in [fd, fd1 ,fd2, ]] 
    return MCFileCollection( mcfs , gd, warn = False)


def cmssm_multinest_all_sessions_comb_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_multinest_all_med_sessions_comb.root" % base_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_all_sessions_comb_histo() :
    return [MCFile(cmssm_multinest_all_sessions_comb_histo_dict() )]


##########################################################################################

def nuhm2_mn_boxes_input(box_n ) :
    # output / global options
    gd = nuhm2_mn_boxes_histo_dict(box_n)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(1, 401):
        fd = {
                 "FileName"          : "%s/%s/cmssm-step-%i.root" % (nuhm2_boxes_directory(),nuhm2_boxes_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_boxes_histo_dict( box_n) :
    d= {
        "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_boxes_directory(), nuhm2_boxes_sub_dirs(box_n) ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 9, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_boxes_histo(box_n) :
    return [MCFile(nuhm2_mn_boxes_histo_dict(box_n) )]

def nuhm2_mn_boxes_histo_range(range_begin, range_end) :
    return [MCFile(nuhm2_mn_boxes_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def nuhm2_mn_boxes_combined_input( ) :
    # output / global options
    gd = nuhm2_mn_boxes_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,32):
        fd = {
                 "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_boxes_directory(), nuhm2_boxes_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_boxes_combined_histo_dict() :
    d= {
        "FileName"          : "%s/nuhm2_all_boxes_combined.root" % (boxes_directory(),  ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_boxes_combined_histo() :
    return [MCFile(nuhm2_mn_boxes_combined_histo_dict() )]


##########################################################################################

def nuhm2_mn_xmas_box_steps_input(box_n,first,last ) :
    # output / global options
    gd = nuhm2_mn_xmas_histo_dict(box_n)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(first,last + 1 ):
        fd = {
                 "FileName"          : "%s/%s/nuhm2-step-%i.root" % (nuhm2_xmas_directory(),nuhm2_xmas_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)

def nuhm2_mn_xmas_box_all_steps_input(box_n) :
    dir=nuhm2_xmas_directory()+'/'+nuhm2_xmas_sub_dirs(box_n)
    print dir
    import os
    steps=[int(f.replace('nuhm2-step-','').replace('.root','')) for f in os.listdir(dir) if 'nuhm2-step-' in f and '.root' in f]
    steps.pop(steps.index(max(steps)))
    gd = nuhm2_mn_xmas_histo_dict(box_n)
    fds=[]
    for step in steps:
        fd = {
                 "FileName"          : "%s/%s/nuhm2-step-%i.root" % (nuhm2_xmas_directory(),nuhm2_xmas_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_xmas_histo_dict( box_n) :
    d= {
        "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_xmas_directory(), nuhm2_xmas_sub_dirs(box_n) ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 9, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_xmas_histo(box_n) :
    return [MCFile(nuhm2_mn_xmas_histo_dict(box_n) )]

def nuhm2_mn_xmas_histo_range(range_begin, range_end) :
    return [MCFile(nuhm2_mn_xmas_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def nuhm2_mn_xmas_combined_input( ) :
    # output / global options
    gd = nuhm2_mn_xmas_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,64):
        fd = {
                 "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_xmas_directory(), nuhm2_xmas_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_xmas_combined_histo_dict() :
    d= {
        "FileName"          : "%s/nuhm2_all_xmas_combined.root" % (nuhm2_xmas_directory(),  ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_xmas_combined_histo() :
    return [MCFile(nuhm2_mn_xmas_combined_histo_dict() )]


##########################################################################################
##########################################################################################

#def nuhm2_mn_ndn_box_steps_input(box_n,first,last ) :
#    # output / global options
#    gd = nuhm2_mn_ndn_histo_dict(box_n)
##    gd["StartEntry"] = 0
##    gd["EndEntry"]   = 50000
#    fds=[]
#    for step in range(first,last + 1 ):
#        fd = {
#                 "FileName"          : "%s/%s/nuhm2-step-%i.root" % (nuhm2_ndn_directory(),nuhm2_ndn_sub_dirs(box_n), step) ,
#                 "Chi2TreeName"      : "tree",
#             }
#        fds.append(fd)
#    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
#    return MCFileCollection(  mcfs , gd, warn = False)

def nuhm2_mn_ndn_box_all_steps_input(box_n) :
    dir=nuhm2_ndn_directory()+'/'+nuhm2_ndn_sub_dirs(box_n)
    print dir
    import os
    steps=[int(f.replace('nuhm2-step-','').replace('.root','')) for f in os.listdir(dir) if 'nuhm2-step-' in f and '.root' in f]
    steps.pop(steps.index(max(steps)))
    gd = nuhm2_mn_ndn_histo_dict(box_n)
    fds=[]
    for step in steps:
        fd = {
                 "FileName"          : "%s/%s/nuhm2-step-%i.root" % (nuhm2_ndn_directory(),nuhm2_ndn_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_ndn_histo_dict( box_n) :
    d= {
        "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_ndn_directory(), nuhm2_ndn_sub_dirs(box_n) ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 9, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_ndn_histo(box_n) :
    return [MCFile(nuhm2_mn_ndn_histo_dict(box_n) )]

def nuhm2_mn_ndn_histo_range(range_begin, range_end) :
    return [MCFile(nuhm2_mn_ndn_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def nuhm2_mn_ndn_combined_input( ) :
    # output / global options
    gd = nuhm2_mn_ndn_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,192):
        fd = {
                 "FileName"          : "%s/%s/nuhm2_all.root" % (nuhm2_ndn_directory(), nuhm2_ndn_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_mn_ndn_combined_histo_dict() :
    d= {
        "FileName"          : "%s/nuhm2_all_ndn_combined.root" % (nuhm2_ndn_directory(),  ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 76,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_mn_ndn_combined_histo() :
    return [MCFile(nuhm2_mn_ndn_combined_histo_dict() )]


##########################################################################################
