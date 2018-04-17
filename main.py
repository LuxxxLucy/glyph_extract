import os
import font_utils

FONT_DIR = "./src"
TTX_DIR = "./ttx"
GLYPH_DIR = './glyph'
if __name__ == "__main__":

    # "ttx " + FONT_NAME + " -d " + TTX_DIR

    # loop through fonts :decode into glyphsself.
    # each glyph consists of more than one contours which consists of a tuple (x_location,y_location,bezier_condition)

    for font_name in os.listdir(FONT_DIR):
        format = font_name.split(".")[-1]
        if format not in ["ttf","otf","TTF","OTF"]:
            continue
        font = font_utils.decode(font_name,ttx_dir=TTX_DIR,input_dir=FONT_DIR)
        print("successfully preprocessing"+font_name)

    print("mission accomplished!")

    # normalize the EM square to be the same. It is essential to do that We constrain it to a 500*500 EM square.

    # get the map from unicode string to glyph ids
