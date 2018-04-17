import cmd # command line tool
import sys # system utilities
import os
from fontTools.ttLib import TTFont
from xml.dom import minidom
from pprint import pprint as pr


def decode(file_name,input_dir="./src",ttx_dir="./ttx",glyph_dir="./glyph"):
    # initialize the glyphs dictionary: key: id -> value: glyph
    glyphs = {}
    file_path = os.path.join(input_dir,file_name)
    output_file_name = file_name.split(".")[0] + ".ttx"
    output_file_path = os.path.join(ttx_dir,output_file_name)
    glyph_file_name = file_name.split(".")[0] + ".glyph"
    glyph_file_path = os.path.join(glyph_dir,output_file_name)

    if not os.path.exists(output_file_path):
        # processing the cmd line tool
        command = "ttx -d " + ttx_dir + " -t \'glyf\' " + file_path
        try:
            os.system(command)
        except:
            print ("command not okay when preprocessing")
            print(command)
            print("check again if there is anything wrong")
            return glyphs

    print("start preprocess glyph")
    # open the xml file and extract the glyphs file
    xmldoc = minidom.parse(output_file_path)
    glyph_list = xmldoc.getElementsByTagName('TTGlyph')
    for character in glyph_list:
        print(character.attributes['name'].value)
        target_contours = []
        for contour in character.getElementsByTagName('contour'):
            target_contour=[]
            for pt in contour.getElementsByTagName('pt'):
                x_location = int(pt.attributes['x'].value)
                y_location = int(pt.attributes['y'].value)
                bezier_condition = int(pt.attributes['on'].value)
                target_contour.append( [x_location,y_location,bezier_condition] )
            target_contours.append(target_contour)
        glyphs[character.attributes['name'].value] = target_contours

    # pr(glyphs)
    # pr(glyphs['uni304F'])
    glyph_save(glyphs)
    return glyphs

def normalize(glyph):
    return glyphs

def render(glyph):
    pass

def glyph_save(name):
    pass

if __name__ == "__main__":
    print("utilities of font manipulation")
