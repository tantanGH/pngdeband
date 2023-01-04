import argparse
import tempfile
import os
import uuid
import ffmpeg

def deband_png(in_file, out_file, resize, width, height, th1, th2, th3, blur):

  with tempfile.TemporaryDirectory() as tmp_dir:
  
    tmp_bmp_file = os.path.join(tmp_dir,str(uuid.uuid1())+".bmp")

    (
      ffmpeg
      .input(in_file, vcodec='png')
      .video
      .filter("deband",blur=blur)
      .output(tmp_bmp_file, vcodec='bmp', pix_fmt='rgb555')
      .global_args('-hide_banner','-loglevel','error')
      .run()
    )

    (
      ffmpeg
      .input(tmp_bmp_file, vcodec='bmp')
      .video
      .output(out_file, vcodec='png', pix_fmt='rgb24')
      .global_args('-hide_banner','-loglevel','error')
      .run()
    )

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("infile",help="input PNG file")
    parser.add_argument("outfile",help="output PNG file")
    parser.add_argument("-r","--resize",help="resize percent",type=int)
    parser.add_argument("-x","--width",help="resize width",type=int)
    parser.add_argument("-y","--height",help="resize height",type=int)
    parser.add_argument("-t1","--threshold1",help="debanding detection threshold for channel 1 (default:0.02)",default=0.02)
    parser.add_argument("-t2","--threshold2",help="debanding detection threshold for channel 2 (default:0.02)",default=0.02)
    parser.add_argument("-t3","--threshold3",help="debanding detection threshold for channel 3 (default:0.02)",default=0.02)
    parser.add_argument("-bl","--blur",help="1:check with average of 4 pixels 0:check with all 4 pixels (default:1)",type=int,default=1)

    args = parser.parse_args()

    deband_png(args.infile, \
               args.outfile, \
               args.resize, \
               args.width, \
               args.height, \
               args.threshold1, \
               args.threshold2, \
               args.threshold3, \
               args.blur)

if __name__ == "__main__":
    main()
