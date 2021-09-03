#!/usr/bin/env python
#    This file is part of python-evtx.
#
#   Copyright 2012, 2013 Willi Ballenthin <william.ballenthin@mandiant.com>
#                    while at Mandiant <http://www.mandiant.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Version v0.1.1
import Evtx.Evtx as evtx
import Evtx.Views as e_views
import sys
import re
#import pandas as pd
#sys.stdout = open('stdout.txt', 'w')
def main():
    import argparse
    sys.stdout = open('sample.txt', 'w')
    parser = argparse.ArgumentParser(
        description="Dump a binary EVTX file into XML.")
    parser.add_argument("evtx", type=str,
                        help="Path to the Windows EVTX event log file")
    args = parser.parse_args()
    
    id_pattern = '201'
    result_pattern = '214794240*'
    r= re.compile(result_pattern)
    
    Tot_count = 0
    E_count = 0
    Comp_Nm =[]
    i=0
    Nm=[]
    with evtx.Evtx(args.evtx) as log:
        #print(e_views.XML_HEADER)
        #print("<Events>")
        for record in log.records():
            xml_st = record.xml()
            if "<Task>201</Task>" in xml_st:
                Tot_count+=1
                if "2147942401" in xml_st:
                    Nm = re.findall('KR_(\S+)_comp', xml_st)
                    #print(Nm[i])
                    Comp_Nm.append(Nm)
                    i+=1
                    E_count += 1
                elif "2147942402" in xml_st:
                    Nm = re.findall('KR_(\S+)_comp', xml_st)
                    Comp_Nm.append(Nm)
                    i+=1
                    E_count += 1
                elif "2147942403" in xml_st:
                    Nm = re.findall('KR_(\S+)_comp', xml_st)
                    Comp_Nm.append(Nm)
                    i+=1
                    E_count += 1
                #print(Nm[i])
        #Comp_Nm = re.findall('\\\\DJ\\\\(\S+)</Data>$', xml_st)
        #Nm = re.findall('<EventData Name="ActionSuccess"><Data Name="TaskName">\DJ\(\S+)</Data>$',xml_st)
        print(Comp_Nm)
        print(Comp_Nm[0][0])
        print(Tot_count)
        print(E_count)
        
        #print("</Events>")
        
    sys.stdout.close()

if __name__ == "__main__":
    main()
