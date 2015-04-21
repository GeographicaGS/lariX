# -*- coding: utf-8 -*-
#  
#  Prettify an XML file with Python (CLI). Useful for really large XML files.
# 
#  Author: Cayetano Benavent, 2015.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 

import argparse
import lxml.etree as etree


def prettifyXML(file_input, fileoutput=None, printscreen=False):
    """
    Prettify an XML file
    
    """
    try:
        
        print "Prettify XML file...\n"
        
        parsedfile = etree.parse(file_input)
        
        pretty_xml = etree.tostring(parsedfile, pretty_print = True)
        
        if printscreen:
            print pretty_xml
        
        else:
            print "Writing new file..."
            
            with open(fileoutput, 'w') as xml_f:
                xml_f.write(pretty_xml)
            
            print "New file successfully created: {0}".format(fileoutput)
    
    except Exception as e:
        print "Error: {0}".format(e.message)


def main():
    
    arg_parser = argparse.ArgumentParser(description='Prettify an XML file')
    
    arg_parser.add_argument('input_XML', type=str, help='input XML file')
    arg_parser.add_argument('-o', '--outputXML', type=str, help='output XML file')
    arg_parser.add_argument('--printscreen', help='print output to screen', action='store_true')
    
    args = arg_parser.parse_args()

    file_input = args.input_XML

    if args.outputXML:
        file_output = args.outputXML
        prettifyXML(file_input, fileoutput=file_output)
        
    elif args.printscreen:
        prettifyXML(file_input, printscreen=True)


if __name__ == '__main__':
    main()
