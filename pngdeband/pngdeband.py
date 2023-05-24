import argparse
import tempfile
import os
import uuid
import ffmpeg

def deband_png(in_file, out_file, resize, width, height, sharp, th1, th2, th3, blur):

  with tempfile.TemporaryDirectory() as tmp_dir:
  

    meta_data = ffmpeg.probe(in_file)

    # Get the video stream information
    video_stream = next(s for s in meta_data['streams'] if s['codec_type'] == 'video')

    # Get the original width and height of the video
    width_orig = int(video_stream['width'])
    height_orig = int(video_stream['height'])

    if width is not None and height is not None:
      width_new = width
      height_new = height
    elif width is not None and height is None:
      width_new = width
      height_new = height_orig * width_new // width_orig
    elif width is None and height is not None:
      height_new = height
      width_new = width_orig * height_new // height_orig
    elif resize is not None:
      width_new = width_orig * resize // 100
      height_new = height_orig * resize // 100
    else:
      width_new = width_orig
      height_new = height_orig

    tmp_bmp_file = os.path.join(tmp_dir,str(uuid.uuid1())+".bmp")

#      .filter("deband", "1thr"={th1}, "2thr"={th2}, "3thr"={th3}, blur={blur}")
    (
      ffmpeg
      .input(in_file, vcodec='png')
      .video
      .filter("scale", width_new, height_new)
      .filter("cas", sharp)
      .output(tmp_bmp_file, vcodec='bmp', pix_fmt='rgb555')
      .global_args('-hide_banner','-loglevel','error','-vf',f"deband=1thr={th1}:2thr={th2}:3thr={th3}:blur={blur}")
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
    parser.add_argument("-x","--width",help="resize width",type=int)
    parser.add_argument("-y","--height",help="resize height",type=int)
    parser.add_argument("-r","--resize",help="resize percent",type=int)
    parser.add_argument("-s","--sharpness",help="sharpness ratio (0.0 to 1.0, default:0.0)",type=float,default=0.0)
    parser.add_argument("-t1","--threshold1",help="band detection threshold for channel 1 (0.00003 to 0.5, default:0.02)",default=0.02)
    parser.add_argument("-t2","--threshold2",help="band detection threshold for channel 2 (0.00003 to 0.5, default:0.02)",default=0.02)
    parser.add_argument("-t3","--threshold3",help="band detection threshold for channel 3 (0.00003 to 0.5, default:0.02)",default=0.02)
    parser.add_argument("-bl","--blur",help="1:check with average of 4 pixels 0:check with all 4 pixels (default:1)",type=int,default=1)

    args = parser.parse_args()

    deband_png(args.infile, \
               args.outfile, \
               args.resize, \
               args.width, \
               args.height, \
               args.sharpness, \
               args.threshold1, \
               args.threshold2, \
               args.threshold3, \
               args.blur)

if __name__ == "__main__":
    main()
