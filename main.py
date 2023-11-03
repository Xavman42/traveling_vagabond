import time

import neoscore.core.neoscore
from neoscore.common import *
from typing import Optional
from classical_solver import multi_knapsack_mip
from Cells import *
import cv2
from PIL import Image

from music_helpers import lock_to_screen, initialize_helpers, unlock_from_screen, move_locked_glyphs, \
    brute_force_tsp, unlock_all_from_screen


def video_from_rendered_images():
    # First, render an image to get the dimensions of the jpg file
    # Full_score_mode
    # scale = 0.4
    # x_screen = -320
    # y_screen = -240
    # dpi = 361
    # Pno_mode
    scale = 0.22
    x_screen = -255
    y_screen = -30
    dpi = 655
    # Vc_mode
    # scale = 0.14
    # x_screen = -255
    # y_screen = -95
    # dpi = 1029
    # Vln_mode
    # scale = 0.14
    # x_screen = -255
    # y_screen = -210
    # dpi = 1029
    # Strings_mode
    # scale = 0.22
    # x_screen = -275
    # y_screen = -200
    # dpi = 655

    neoscore.render_image(Rect(Unit(initial_x + x_screen), Unit(initial_y + y_screen), Unit(1920 * scale), Unit(1080 * scale)), "tmp.jpg",
                          quality=100, dpi=dpi)
    image = Image.open("tmp.jpg")
    width = image.size[0]
    height = image.size[1]

    # Define video format
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create video writer ("name", format, fps, (width, height))
    video = cv2.VideoWriter("video_name.mp4", fourcc, fps, (width, height))

    # Iterate over every frame in the video
    for frame in range(0, round(fps * duration)):
        # Do desired neoscore animations
        ti = animate(frame)

        # Render an image to file using same dimensions as earlier test and open it
        neoscore.render_image(
            Rect(Unit(initial_x + x_screen + ti * zoom), Unit(initial_y + y_screen), Unit(1920 * scale), Unit(1080 * scale)), "tmp.jpg",
            quality=100, dpi=dpi)
        img = Image.open("tmp.jpg")

        # Monitor video render time - this is a very slow method of video rendering
        print(str(round(frame / fps, 2)) + " seconds")

        # Write the frame to the end of the video stream
        video.write(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    video.release()


# def refresh_func(this_time: float) -> Optional[neoscore.RefreshFuncResult]:
def animate(frame):
    global prev_loc
    move_rate = zoom
    # t = (this_time - start_time)/2
    t = frame / fps
    move_locked_glyphs()
    neoscore.set_viewport_center_pos((Unit(initial_x + t * move_rate), Unit(initial_y)))
    art_offset = 0.7

    piece_loc = (neoscore.get_viewport_center_pos().x + reticle_pos) / zoom
    if piece_loc.base_value > 0.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_0_vln)
        if render_vc: lock_to_screen(dynamic_0_vc)
        if render_pno: lock_to_screen(dynamic_0_pno)
    elif piece_loc.base_value > 25.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_0_vc)
    elif piece_loc.base_value > 31.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_0_vln)
    elif piece_loc.base_value > 35.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_0_pno)
        if render_vln: lock_to_screen(dynamic_35_vln)
    elif piece_loc.base_value > 39.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_35_vln)
    elif piece_loc.base_value > 43.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_43_vc)
    elif piece_loc.base_value > 44.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_44_vln)
        if render_pno: lock_to_screen(dynamic_44_pno)
    elif piece_loc.base_value > 45.25 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_43_vc)
        if render_vc: lock_to_screen(dynamic_45_vc)
        if render_vc: unlock_from_screen(clef_vc)
        if render_vc: lock_to_screen(clef_vc_2)
    elif piece_loc.base_value > 48.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_44_vln)
    elif piece_loc.base_value > 49.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_44_pno)
    elif piece_loc.base_value > 51.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_51_vln)
    elif piece_loc.base_value > 53.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_45_vc)
        if render_pno: lock_to_screen(dynamic_53_pno)
    elif piece_loc.base_value > 55.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_55_vc)
    elif piece_loc.base_value > 65.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_55_vc)
        if render_pno: unlock_from_screen(dynamic_53_pno)
        if render_pno: lock_to_screen(dynamic_65_pno)
    elif piece_loc.base_value > 67.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_51_vln)
    elif piece_loc.base_value > 69.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_69_vc)
    elif piece_loc.base_value > 73.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_73_vln)
    elif piece_loc.base_value > 86.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_69_vc)
    elif piece_loc.base_value > 90.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_73_vln)
        if render_pno: unlock_from_screen(dynamic_65_pno)
        if render_vln: lock_to_screen(dynamic_90_vln)
        if render_vc: lock_to_screen(dynamic_90_vc)
        if render_pno: lock_to_screen(dynamic_90_pno)
    elif piece_loc.base_value > 91.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_90_vln)
        if render_vln: lock_to_screen(dynamic_91_vln)
    elif piece_loc.base_value > 95.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_90_vc)
    elif piece_loc.base_value > 97.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_91_vln)
    elif piece_loc.base_value > 100.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_100_vc)
    elif piece_loc.base_value > 101.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_101_vln)
    elif piece_loc.base_value > 110.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_90_pno)
        if render_pno: lock_to_screen(dynamic_110_pno)
    elif piece_loc.base_value > 123.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_100_vc)
    elif piece_loc.base_value > 124.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_110_pno)
    elif piece_loc.base_value > 126.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_126_vc)
    elif piece_loc.base_value > 129.2 > prev_loc.base_value:
        if render_pno: lock_to_screen(dynamic_129_pno)
    elif piece_loc.base_value > 131.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_126_vc)
    elif piece_loc.base_value > 134.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_129_pno)
        if render_vc: lock_to_screen(dynamic_134_vc)
    elif piece_loc.base_value > 138.2 > prev_loc.base_value:
        if render_pno: lock_to_screen(dynamic_138_pno)
    elif piece_loc.base_value > 142.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_138_pno)
    elif piece_loc.base_value > 147.2 > prev_loc.base_value:
        if render_pno: lock_to_screen(dynamic_147_pno)
    elif piece_loc.base_value > 150.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_101_vln)
        if render_vc: unlock_from_screen(dynamic_134_vc)
        if render_pno: unlock_from_screen(dynamic_147_pno)
        if render_vln: lock_to_screen(dynamic_150_vln)
        if render_vc: lock_to_screen(dynamic_150_vc)
        if render_pno: lock_to_screen(dynamic_150_pno)
    elif piece_loc.base_value > 154.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_150_pno)
    elif piece_loc.base_value > 155.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_150_vc)
    elif piece_loc.base_value > 156.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_150_vln)
    elif piece_loc.base_value > 158.2 > prev_loc.base_value:
        if render_pno: lock_to_screen(dynamic_158_pno)
    elif piece_loc.base_value > 159.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_159_vc)
    elif piece_loc.base_value > 167.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_159_vc)
    elif piece_loc.base_value > 171.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_171_vc)
    elif piece_loc.base_value > 172.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_172_vln)
    elif piece_loc.base_value > 180.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_171_vc)
    elif piece_loc.base_value > 187.2 > prev_loc.base_value:
        if render_vc: lock_to_screen(dynamic_187_vc)
    elif piece_loc.base_value > 203.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_172_vln)
    elif piece_loc.base_value > 209.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_209_vln)
    elif piece_loc.base_value > 210.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_209_vln)
        if render_vc: unlock_from_screen(dynamic_187_vc)
        if render_pno: unlock_from_screen(dynamic_158_pno)
        if render_vln: lock_to_screen(dynamic_210_vln)
        if render_vc: lock_to_screen(dynamic_210_vc)
        if render_pno: lock_to_screen(dynamic_210_pno)
    elif piece_loc.base_value > 223.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_210_vc)
    elif piece_loc.base_value > 225.2 > prev_loc.base_value:
        if render_vln:unlock_from_screen(dynamic_210_vln)
    elif piece_loc.base_value > 230.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_210_pno)
        if render_vln: lock_to_screen(dynamic_230_vln)
        if render_vc: lock_to_screen(dynamic_230_vc)
        if render_pno: lock_to_screen(dynamic_230_pno)
    elif piece_loc.base_value > 235.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_230_vc)
    elif piece_loc.base_value > 238.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_230_vln)
    elif piece_loc.base_value > 239.2 > prev_loc.base_value:
        if render_pno: unlock_from_screen(dynamic_230_pno)
    elif piece_loc.base_value > 240.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_240_vln)
        if render_vc: lock_to_screen(dynamic_240_vc)
        if render_pno: lock_to_screen(dynamic_240_pno)
    elif piece_loc.base_value > 250.2 > prev_loc.base_value:
        if render_vln: unlock_from_screen(dynamic_240_vln)
    elif piece_loc.base_value > 258.2 > prev_loc.base_value:
        if render_vc: unlock_from_screen(dynamic_240_vc)
        if render_pno: unlock_from_screen(dynamic_240_pno)
    elif piece_loc.base_value > 262.2 > prev_loc.base_value:
        if render_vln: lock_to_screen(dynamic_262_vln)
        if render_vc: lock_to_screen(dynamic_262_vc)
        if render_pno: lock_to_screen(dynamic_262_pno)
    elif piece_loc.base_value > 0 + art_offset > prev_loc.base_value:
        if render_vln: lock_to_screen(bow_0_vln)
        if render_vc: lock_to_screen(bow_0_vc)
    elif piece_loc.base_value > 11 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_0_vln)
        if render_vln: lock_to_screen(bow_11_vln)
    elif piece_loc.base_value > 30 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_11_vln)
        if render_vln: lock_to_screen(bow_30_vln)
    elif piece_loc.base_value > 37 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_0_vc)
        if render_vc: lock_to_screen(bow_37_vc)
    elif piece_loc.base_value > 44 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_30_vln)
        if render_vln: lock_to_screen(bow_44_vln)
    elif piece_loc.base_value > 45 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_44_vln)
        if render_vln: lock_to_screen(bow_45_vln)
        if render_vc: unlock_from_screen(bow_37_vc)
        if render_vc: lock_to_screen(bow_45_vc)
    elif piece_loc.base_value > 55 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_45_vc)
        if render_vc: lock_to_screen(bow_55_vc)
    elif piece_loc.base_value > 57 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_55_vc)
        if render_vc: lock_to_screen(bow_57_vc)
    elif piece_loc.base_value > 58 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_45_vln)
        if render_vln: lock_to_screen(bow_58_vln)
    elif piece_loc.base_value > 60 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_57_vc)
        if render_vc: lock_to_screen(bow_60_vc)
    elif piece_loc.base_value > 69 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_60_vc)
        if render_vc: lock_to_screen(bow_69_vc)
    elif piece_loc.base_value > 73 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_58_vln)
        if render_vln: lock_to_screen(bow_73_vln)
    elif piece_loc.base_value > 79 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_69_vc)
        if render_vc: lock_to_screen(bow_79_vc)
    elif piece_loc.base_value > 90 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_73_vln)
        if render_vln: lock_to_screen(bow_90_vln)
        if render_vc: unlock_from_screen(bow_79_vc)
        if render_vc: lock_to_screen(bow_90_vc)
    elif piece_loc.base_value > 100 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_90_vc)
        if render_vc: lock_to_screen(bow_100_vc)
    elif piece_loc.base_value > 101 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_90_vln)
        if render_vln: lock_to_screen(bow_101_vln)
    elif piece_loc.base_value > 103 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_100_vc)
        if render_vc: lock_to_screen(bow_103_vc)
    elif piece_loc.base_value > 106 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_103_vc)
        if render_vc: lock_to_screen(bow_106_vc)
    elif piece_loc.base_value > 109 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_106_vc)
        if render_vc: lock_to_screen(bow_109_vc)
    elif piece_loc.base_value > 112 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_109_vc)
        if render_vc: lock_to_screen(bow_112_vc)
    elif piece_loc.base_value > 126 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_112_vc)
        if render_vc: lock_to_screen(bow_126_vc)
    elif piece_loc.base_value > 127 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_101_vln)
        if render_vln: lock_to_screen(bow_127_vln)
    elif piece_loc.base_value > 141 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_126_vc)
        if render_vc: lock_to_screen(bow_141_vc)
    elif piece_loc.base_value > 150 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_127_vln)
        if render_vln: lock_to_screen(bow_150_vln)
        if render_vc: unlock_from_screen(bow_141_vc)
        if render_vc: lock_to_screen(bow_150_vc)
    elif piece_loc.base_value > 159 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_150_vc)
        if render_vc: lock_to_screen(bow_159_vc)
    elif piece_loc.base_value > 165 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_159_vc)
        if render_vc: lock_to_screen(bow_165_vc)
    elif piece_loc.base_value > 171 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_165_vc)
        if render_vc: lock_to_screen(bow_171_vc)
    elif piece_loc.base_value > 172 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_150_vln)
        if render_vln: lock_to_screen(bow_172_vln)
    elif piece_loc.base_value > 187 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_172_vln)
        if render_vln: lock_to_screen(bow_187_vln)
    elif piece_loc.base_value > 198 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_187_vln)
        if render_vln: lock_to_screen(bow_198_vln)
    elif piece_loc.base_value > 200 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_171_vc)
        if render_vc: lock_to_screen(bow_200_vc)
    elif piece_loc.base_value > 208 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_198_vln)
        if render_vln: lock_to_screen(bow_208_vln)
    elif piece_loc.base_value > 209 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_208_vln)
        if render_vln: lock_to_screen(bow_209_vln)
    elif piece_loc.base_value > 210 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_200_vc)
    elif piece_loc.base_value > 218 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_209_vln)
        if render_vln: lock_to_screen(bow_218_vln)
    elif piece_loc.base_value > 225 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_218_vln)
        if render_vln: lock_to_screen(bow_225_vln)
    elif piece_loc.base_value > 235 + art_offset > prev_loc.base_value:
        if render_vc: lock_to_screen(bow_235_vc)
    elif piece_loc.base_value > 240 + art_offset > prev_loc.base_value:
        if render_vc: unlock_from_screen(bow_235_vc)
    elif piece_loc.base_value > 250 + art_offset > prev_loc.base_value:
        if render_vln: unlock_from_screen(bow_225_vln)
        if render_vln: lock_to_screen(bow_250_vln)
    elif piece_loc.base_value > 52.3 + art_offset > prev_loc.base_value:
        if render_pno: lock_to_screen(pedal_53_on)
    elif piece_loc.base_value > 62.3 + art_offset > prev_loc.base_value:
        if render_pno: unlock_from_screen(pedal_53_on)
    elif piece_loc.base_value > 64.3 + art_offset > prev_loc.base_value:
        if render_pno: lock_to_screen(pedal_65_on)
    elif piece_loc.base_value > 87.3 + art_offset > prev_loc.base_value:
        if render_pno: unlock_from_screen(pedal_65_on)
    elif piece_loc.base_value > 109.3 + art_offset > prev_loc.base_value:
        if render_pno: lock_to_screen(pedal_110_on)
    elif piece_loc.base_value > 127.3 + art_offset > prev_loc.base_value:
        if render_pno: unlock_from_screen(pedal_110_on)
    elif piece_loc.base_value > 209.3 + art_offset > prev_loc.base_value:
        if render_pno: lock_to_screen(pedal_210_on)
    elif piece_loc.base_value > 267.3 + art_offset > prev_loc.base_value:
        if render_pno: unlock_from_screen(pedal_210_on)
    elif piece_loc.base_value > 270 > prev_loc.base_value:
        unlock_all_from_screen()
    prev_loc = piece_loc
    return t


neoscore.setup()
# neoscore.set_default_color("#ffffff")
# neoscore.set_background_brush("#222222")
initialize_helpers()
# Create bounding box for piece
Path.rect((Mm(-100000), Mm(-100000)), None, Mm(200000), Mm(200000),
          Brush.no_brush(), Pen.no_pen())
render_vln = False
render_vc = False
render_pno = True

zoom = 100
horiz_offset = -80
# Create staves + clefs + inst. names + brace
if render_vln:
    staff_vln = Staff((Mm(horiz_offset), Mm(0)), None, Mm(500))
    clef_vln = Clef(ZERO, staff_vln, 'treble')
    lock_to_screen(clef_vln)
    vln_name = InstrumentName((Mm(horiz_offset + 8), staff_vln.center_y + Mm(-10)), staff_vln, "Violin", "Vln.")
    lock_to_screen(vln_name)

if render_vc:
    staff_vc = Staff((Mm(horiz_offset), Mm(35)), None, Mm(500))
    clef_vc = Clef(ZERO, staff_vc, 'treble')
    lock_to_screen(clef_vc)
    vc_name = InstrumentName((Mm(horiz_offset + 8), staff_vc.center_y + Mm(25)), staff_vc, "Cello", "Vc.")
    lock_to_screen(vc_name)
    clef_vc_2 = Clef(Unit(zoom * 45) - Mm(horiz_offset + 10), staff_vc, 'bass')

if render_pno:
    piano_group = StaffGroup()
    staff_treble = Staff((Mm(horiz_offset), Mm(70)), None, Mm(500), piano_group)
    clef_treble = Clef(ZERO, staff_treble, 'treble')
    lock_to_screen(clef_treble)
    staff_bass = Staff((Mm(horiz_offset), Mm(85)), None, Mm(0), piano_group)
    clef_bass = Clef(ZERO, staff_bass, 'bass')
    lock_to_screen(clef_bass)
    brace = Brace(piano_group)
    lock_to_screen(brace)
    pno_name = InstrumentName((Mm(horiz_offset + 8), brace.center_y + Mm(50)), staff_treble, "Piano", "Pno.")
    lock_to_screen(pno_name)

reticle_pos = Mm(-60)
reticle = Path.straight_line((reticle_pos, Mm(-100)), None, (Mm(0), Mm(300)),
                             pen=Pen(thickness=Mm(0.5), pattern=PenPattern.SOLID))
lock_to_screen(reticle)

# Section 1 Dynamics
if render_vln:
    dynamic_0_vln = Dynamic((Unit(zoom * 0) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "pp")
    dynamic_30_vln = Dynamic((Unit(zoom * 30) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "p")
    dynamic_35_vln = Dynamic((Unit(zoom * 35) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "mf")
    dynamic_44_vln = Dynamic((Unit(zoom * 44) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "f")
if render_vc:
    dynamic_0_vc = Dynamic((Unit(zoom * 0) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "pp")
    dynamic_37_vc = Dynamic((Unit(zoom * 37) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mp")
    dynamic_43_vc = Dynamic((Unit(zoom * 43) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mf")
if render_pno:
    dynamic_0_pno = Dynamic((Unit(zoom * 0) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "pp")
    dynamic_44_pno = Dynamic((Unit(zoom * 44) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "f")

# Section 2 Dynamics
if render_vln:
    dynamic_51_vln = Dynamic((Unit(zoom * 51) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "mf")
    dynamic_73_vln = Dynamic((Unit(zoom * 73) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "p")
if render_vc:
    dynamic_45_vc = Dynamic((Unit(zoom * 45) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "ff")
    dynamic_55_vc = Dynamic((Unit(zoom * 55) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "f")
    dynamic_69_vc = Dynamic((Unit(zoom * 69) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mp")
if render_pno:
    dynamic_53_pno = Dynamic((Unit(zoom * 53) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "mf")
    dynamic_65_pno = Dynamic((Unit(zoom * 65) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "p")

# Section 3 Dynamics
if render_vln:
    dynamic_90_vln = Dynamic((Unit(zoom * 90) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "ff")
    dynamic_91_vln = Dynamic((Unit(zoom * 91) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "f")
    dynamic_101_vln = Dynamic((Unit(zoom * 101) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "mp")
if render_vc:
    dynamic_90_vc = Dynamic((Unit(zoom * 90) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "f")
    dynamic_100_vc = Dynamic((Unit(zoom * 100) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mp")
    dynamic_126_vc = Dynamic((Unit(zoom * 126) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "f")
    dynamic_134_vc = Dynamic((Unit(zoom * 134) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mp")
if render_pno:
    dynamic_90_pno = Dynamic((Unit(zoom * 90) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "f")
    dynamic_110_pno = Dynamic((Unit(zoom * 110) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "mp")
    dynamic_129_pno = Dynamic((Unit(zoom * 129) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "f")
    dynamic_138_pno = Dynamic((Unit(zoom * 138) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "pp")
    dynamic_147_pno = Dynamic((Unit(zoom * 147) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "ff")

# Section 4 Dynamics
if render_vln:
    dynamic_150_vln = Dynamic((Unit(zoom * 150) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "ff")
    dynamic_172_vln = Dynamic((Unit(zoom * 172) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "p")
    dynamic_206_vln = Dynamic((Unit(zoom * 206) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "mf")
    dynamic_209_vln = Dynamic((Unit(zoom * 209) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "ff")
if render_vc:
    dynamic_150_vc = Dynamic((Unit(zoom * 150) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "ff")
    dynamic_159_vc = Dynamic((Unit(zoom * 159) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "p")
    dynamic_171_vc = Dynamic((Unit(zoom * 171) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "f")
    dynamic_187_vc = Dynamic((Unit(zoom * 187) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "p")
if render_pno:
    dynamic_150_pno = Dynamic((Unit(zoom * 150) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass, "ff")
    dynamic_158_pno = Dynamic((Unit(zoom * 158) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass, "p")

# Section 5 Dynamics
if render_vln:
    dynamic_210_vln = Dynamic((Unit(zoom * 210) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "fff")
    dynamic_230_vln = Dynamic((Unit(zoom * 230) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "f")
if render_vc:
    dynamic_210_vc = Dynamic((Unit(zoom * 210) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "fff")
    dynamic_230_vc = Dynamic((Unit(zoom * 230) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "f")
if render_pno:
    dynamic_210_pno = Dynamic((Unit(zoom * 210) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass, "fff")
    dynamic_230_pno = Dynamic((Unit(zoom * 230) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass, "f")

# Section 6 Dynamics
if render_vln:
    dynamic_240_vln = Dynamic((Unit(zoom * 240) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "mp")
    dynamic_262_vln = Dynamic((Unit(zoom * 262) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln, "pp")
if render_vc:
    dynamic_240_vc = Dynamic((Unit(zoom * 240) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "mp")
    dynamic_262_vc = Dynamic((Unit(zoom * 262) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc, "pp")
if render_pno:
    dynamic_240_pno = Dynamic((Unit(zoom * 240) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass, "mp")
    dynamic_262_pno = Dynamic((Unit(zoom * 262) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble, "pp")

# Vln Hairpins
if render_vln:
    Hairpin((Unit(zoom * 30.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 4.6), ZERO))
    Hairpin((Unit(zoom * 39.0) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 4.8), ZERO))
    Hairpin((Unit(zoom * 48.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 2.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 67.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 5.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 97.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 156.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 15.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 203.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 2.6), ZERO))
    Hairpin((Unit(zoom * 206.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 2.6), ZERO))
    Hairpin((Unit(zoom * 225.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 4.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 238.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 1.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 250.2) - Mm(horiz_offset), staff_vln.unit(8)), staff_vln,
            (Unit(zoom * 11.6), ZERO), direction=DirectionX.LEFT)

# Vc Hairpins
if render_vc:
    Hairpin((Unit(zoom * 25.0) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 11.8), ZERO))
    Hairpin((Unit(zoom * 37.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 5.6), ZERO))
    Hairpin((Unit(zoom * 53.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 1.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 65.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 86.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 95.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 4.6), ZERO))
    Hairpin((Unit(zoom * 123.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 2.6), ZERO))
    Hairpin((Unit(zoom * 131.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 2.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 155.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 167.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 3.6), ZERO))
    Hairpin((Unit(zoom * 180.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 6.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 223.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 6.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 235.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 4.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 258.2) - Mm(horiz_offset), staff_vc.unit(8)), staff_vc,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)

# Pno Hairpins
if render_pno:
    Hairpin((Unit(zoom * 35.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 8.6), ZERO))
    Hairpin((Unit(zoom * 49.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 124.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 4.6), ZERO))
    Hairpin((Unit(zoom * 134.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 142.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 4.6), ZERO))
    Hairpin((Unit(zoom * 154.2) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 239.2) - Mm(horiz_offset), staff_bass.unit(8)), staff_bass,
            (Unit(zoom * 0.6), ZERO), direction=DirectionX.LEFT)
    Hairpin((Unit(zoom * 258.2) - Mm(horiz_offset), staff_treble.unit(8)), staff_treble,
            (Unit(zoom * 3.6), ZERO), direction=DirectionX.LEFT)

# Bow markings
if render_vln:
    bow_0_vln = Text((Unit(zoom * 0) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                     "molto pont.", neoscore.default_font.modified(italic=True))
    bow_11_vln = Text((Unit(zoom * 11) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                      "pont.", neoscore.default_font.modified(italic=True))
    bow_30_vln = Text((Unit(zoom * 30) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "ord.", neoscore.default_font.modified(italic=True))
    bow_44_vln = Text((Unit(zoom * 44) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "pont.", neoscore.default_font.modified(italic=True))
    bow_45_vln = Text((Unit(zoom * 45) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "ord.", neoscore.default_font.modified(italic=True))
    bow_58_vln = Text((Unit(zoom * 58) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "molto tasto", neoscore.default_font.modified(italic=True))
    bow_73_vln = Text((Unit(zoom * 73) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "pizz.", neoscore.default_font.modified(italic=True))
    bow_90_vln = Text((Unit(zoom * 90) - Mm(horiz_offset), staff_vln.unit(-8)), staff_vln,
                      "arco", neoscore.default_font.modified(italic=True))
    bow_90_vln = Text((Unit(zoom * 90) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                      "pont.", neoscore.default_font.modified(italic=True))
    bow_101_vln = Text((Unit(zoom * 101) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "molto pont.", neoscore.default_font.modified(italic=True))
    bow_127_vln = Text((Unit(zoom * 127) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "pizz.", neoscore.default_font.modified(italic=True))
    bow_150_vln = Text((Unit(zoom * 150) - Mm(horiz_offset), staff_vln.unit(-10)), staff_vln,
                       "arco", neoscore.default_font.modified(italic=True))
    bow_150_vln = Text((Unit(zoom * 150) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                       "ord.", neoscore.default_font.modified(italic=True))
    bow_172_vln = Text((Unit(zoom * 172) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "molto pont.", neoscore.default_font.modified(italic=True))
    bow_187_vln = Text((Unit(zoom * 187) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                       "molto tasto", neoscore.default_font.modified(italic=True))
    bow_198_vln = Text((Unit(zoom * 198) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "ord.", neoscore.default_font.modified(italic=True))
    bow_208_vln = Text((Unit(zoom * 208) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "pont.", neoscore.default_font.modified(italic=True))
    bow_209_vln = Text((Unit(zoom * 209) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "molto pont.", neoscore.default_font.modified(italic=True))
    bow_218_vln = Text((Unit(zoom * 218) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                       "pont.", neoscore.default_font.modified(italic=True))
    bow_225_vln = Text((Unit(zoom * 225) - Mm(horiz_offset), staff_vln.unit(-7)), staff_vln,
                       "ord.", neoscore.default_font.modified(italic=True))
    bow_250_vln = Text((Unit(zoom * 250) - Mm(horiz_offset), staff_vln.unit(-5)), staff_vln,
                       "pizz.", neoscore.default_font.modified(italic=True))
if render_vc:
    bow_0_vc = Text((Unit(zoom * 0) - Mm(horiz_offset), staff_vc.unit(-7)), staff_vc,
                    "molto pont.", neoscore.default_font.modified(italic=True))
    bow_37_vc = Text((Unit(zoom * 37) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "pizz.", neoscore.default_font.modified(italic=True))
    bow_45_vc = Text((Unit(zoom * 45) - Mm(horiz_offset), staff_vc.unit(-8)), staff_vc,
                     "arco", neoscore.default_font.modified(italic=True))
    bow_45_vc = Text((Unit(zoom * 45) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "ord.", neoscore.default_font.modified(italic=True))
    bow_55_vc = Text((Unit(zoom * 55) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "tasto", neoscore.default_font.modified(italic=True))
    bow_57_vc = Text((Unit(zoom * 57) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "molto pont.", neoscore.default_font.modified(italic=True))
    bow_60_vc = Text((Unit(zoom * 60) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "ord.", neoscore.default_font.modified(italic=True))
    bow_69_vc = Text((Unit(zoom * 69) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "pont.", neoscore.default_font.modified(italic=True))
    bow_79_vc = Text((Unit(zoom * 79) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                     "molto pont.", neoscore.default_font.modified(italic=True))
    bow_90_vc = Text((Unit(zoom * 90) - Mm(horiz_offset), staff_vc.unit(-7)), staff_vc,
                     "ord.", neoscore.default_font.modified(italic=True))
    bow_100_vc = Text((Unit(zoom * 100) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "molto pont.", neoscore.default_font.modified(italic=True))
    bow_103_vc = Text((Unit(zoom * 103) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "pont.", neoscore.default_font.modified(italic=True))
    bow_106_vc = Text((Unit(zoom * 106) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "ord.", neoscore.default_font.modified(italic=True))
    bow_109_vc = Text((Unit(zoom * 109) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "tasto", neoscore.default_font.modified(italic=True))
    bow_112_vc = Text((Unit(zoom * 112) - Mm(horiz_offset), staff_vc.unit(-7)), staff_vc,
                      "molto tasto", neoscore.default_font.modified(italic=True))
    bow_126_vc = Text((Unit(zoom * 126) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "ord.", neoscore.default_font.modified(italic=True))
    bow_141_vc = Text((Unit(zoom * 141) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "pizz.", neoscore.default_font.modified(italic=True))
    bow_150_vc = Text((Unit(zoom * 150) - Mm(horiz_offset), staff_vc.unit(-10)), staff_vc,
                      "arco", neoscore.default_font.modified(italic=True))
    bow_150_vc = Text((Unit(zoom * 150) - Mm(horiz_offset), staff_vc.unit(-7)), staff_vc,
                      "pont.", neoscore.default_font.modified(italic=True))
    bow_159_vc = Text((Unit(zoom * 159) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "molto pont.", neoscore.default_font.modified(italic=True))
    bow_165_vc = Text((Unit(zoom * 165) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "tasto", neoscore.default_font.modified(italic=True))
    bow_171_vc = Text((Unit(zoom * 171) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "ord.", neoscore.default_font.modified(italic=True))
    bow_200_vc = Text((Unit(zoom * 200) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "pizz.", neoscore.default_font.modified(italic=True))
    bow_210_vc = Text((Unit(zoom * 210) - Mm(horiz_offset), staff_vc.unit(-7)), staff_vc,
                      "arco", neoscore.default_font.modified(italic=True))
    bow_235_vc = Text((Unit(zoom * 235) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "pizz.", neoscore.default_font.modified(italic=True))
    bow_240_vc = Text((Unit(zoom * 240) - Mm(horiz_offset), staff_vc.unit(-5)), staff_vc,
                      "arco", neoscore.default_font.modified(italic=True))

# Pedal markings
if render_pno:
    pedal_45_on = MusicText((Unit(zoom * 45) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_46_off = MusicText((Unit(zoom * 46.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_47_on = MusicText((Unit(zoom * 47) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_48_off = MusicText((Unit(zoom * 48.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_49_on = MusicText((Unit(zoom * 49) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_50_off = MusicText((Unit(zoom * 50.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_51_on = MusicText((Unit(zoom * 51) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_52_off = MusicText((Unit(zoom * 52.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_53_on = MusicText((Unit(zoom * 53) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_64_off = MusicText((Unit(zoom * 64.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_65_on = MusicText((Unit(zoom * 65) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                            "keyboardPedalPed")
    pedal_89_off = MusicText((Unit(zoom * 89.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalUp")
    pedal_110_on = MusicText((Unit(zoom * 110) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                             "keyboardPedalPed")
    pedal_129_off = MusicText((Unit(zoom * 129.5) - Mm(horiz_offset), staff_treble.unit(12)), staff_treble,
                              "keyboardPedalUp")
    pedal_210_on = MusicText((Unit(zoom * 210) - Mm(horiz_offset), staff_bass.unit(12)), staff_bass, "keyboardPedalPed")
    pedal_269_off = MusicText((Unit(zoom * 269.5) - Mm(horiz_offset), staff_bass.unit(12)), staff_bass,
                              "keyboardPedalUp")

    ottava_241 = OctaveLine((Unit(zoom * 241) - Mm(horiz_offset), staff_treble.unit(-4)), staff_treble, Unit(zoom * 14))
    ottava_257 = OctaveLine((Unit(zoom * 257) - Mm(horiz_offset), staff_treble.unit(-4)), staff_treble, Unit(zoom * 13),
                            indication='15ma')

# Section 1 TSP
data = {'weights': (np.arange(1, 45)).tolist(),
        'values': (np.arange(2, 46)).tolist(),
        'bin capacities': [45, 45, 45]}
bins, bins_packed_value, bins_packed_weight = \
    multi_knapsack_mip(data['weights'], data['values'], data['bin capacities'])
print(bins)

# character - complexity space
coord = np.array([
    [0, 0],
    [0.3, 0.4],
    [0.2, 0.2],
    [0.4, 0.3],
    [0.8, 1],
    [0.5, 0.8],
    [0.1, 0.1],
    [1, 0.1]
])

tr_mat = np.zeros([len(coord), len(coord)])
for i in range(len(coord)):
    for j in range(len(coord)):
        tr_mat[i, j] = np.linalg.norm(coord[i] - coord[j])

print(tr_mat)

best_distance, best_order_1 = brute_force_tsp(tr_mat, len(coord))
print(
    "Best order from brute force = "
    + str(best_order_1)
    + " with total distance = "
    + str(best_distance)
)

num_func_map_1 = {
    0: draw_cell_1_1,
    1: draw_cell_1_2,
    2: draw_cell_1_3,
    3: draw_cell_1_4,
    4: draw_cell_1_5,
    5: draw_cell_1_6,
    6: draw_cell_1_7,
    7: draw_cell_1_8,
}

# Section 1 render cells
sca = "chromatic_c"
if render_vln:
    cum = 0
    inst = "vln"
    for idx, i in enumerate(bins['bin_1'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * cum), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_1'])) - idx / len(bins['bin_1']))
        num_func_map_1[best_order_1[idx]](staff_1, width, sus, sca, 2, inst)
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    inst = "vc"
    for idx, i in enumerate(bins['bin_0'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * cum), Mm(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        num_func_map_1[best_order_1[idx]](staff_1, width, sus, sca, 1, inst)
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    inst = "pno"
    for idx, i in enumerate(bins['bin_2'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * cum), Mm(staff_treble.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        num_func_map_1[best_order_1[idx]](staff_1, width, sus, sca, 2, inst)
        cum = cum + (i - 1)

# Section 2 TSP
# character - complexity space
coord = np.array([
    [2, 0],
    [2.1, 0.1],
    [2.2, 0.8],
    [2.15, 0.3],
    [2.6, 0.2],
    [2.8, 0.4],
    [2.5, 0.9],
    [2.65, 0.5]
])

tr_mat = np.zeros([len(coord), len(coord)])
for i in range(len(coord)):
    for j in range(len(coord)):
        tr_mat[i, j] = np.linalg.norm(coord[i] - coord[j])

print(tr_mat)

best_distance, best_order_2 = brute_force_tsp(tr_mat, len(coord))
print(
    "Best order from brute force = "
    + str(best_order_2)
    + " with total distance = "
    + str(best_distance)
)

num_func_map_2 = {
    0: draw_cell_2_1,
    1: draw_cell_2_2,
    2: draw_cell_2_3,
    3: draw_cell_2_4,
    4: draw_cell_2_5,
    5: draw_cell_2_6,
    6: draw_cell_2_7,
    7: draw_cell_2_8,
}

# Section 2 render cells
sus = 0.5
sca = "octatonic[0,1]"
if render_vln:
    cum = 0
    inst = "vln"
    for idx, i in enumerate(bins['bin_2']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 45)), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, 1, inst)
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    inst = "vc"
    for idx, i in enumerate(bins['bin_1']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 45)), Mm(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(bins['bin_1'])) - idx / len(bins['bin_1']))
        num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, -1, inst)
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    inst = "pno"
    for idx, i in enumerate(bins['bin_0']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 45)), Mm(staff_treble.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, 1, inst)
        cum = cum + (i - 1)

# Section 3 TSP
data = {'weights': (np.power(np.arange(0, 119) / 5, 2) + 1).tolist(),
        'values': (np.power(np.arange(0, 119) / 5, 2) + 2).tolist(),
        'bin capacities': [60, 60, 60]}
bins, bins_packed_value, bins_packed_weight = \
    multi_knapsack_mip(data['weights'], data['values'], data['bin capacities'])
print(bins)

# Section 3 render cells
sus = 0.5
sca = "octatonic[0,1]"
if render_vln:
    cum = 0
    toggle = True
    inst = "vln"
    for idx, i in enumerate(bins['bin_2']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 90)), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = True
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    toggle = True
    inst = "vc"
    roll_bin = np.roll(bins['bin_1'], 3)
    for idx, i in enumerate(roll_bin):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 90)), Unit(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(roll_bin)) - idx / len(roll_bin))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, 0, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, 0, inst)
            toggle = True
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    inst = "pno"
    toggle = True
    for idx, i in enumerate(bins['bin_0'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 90)), Unit(staff_treble.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = True
        cum = cum + (i - 1)

sus = 0.5
sca = "hexatonic[0,1]"
if render_vln:
    cum = 0
    inst = "vln"
    toggle = True
    for idx, i in enumerate(bins['bin_2'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 150)), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, 1, inst)
            toggle = True
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    inst = "vc"
    toggle = True
    roll_bin = np.roll(bins['bin_1'], 3)
    for idx, i in enumerate(roll_bin[::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 150)), Unit(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(roll_bin)) - idx / len(roll_bin))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, 0, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, 0, inst)
            toggle = True
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    toggle = True
    inst = "pno"
    for idx, i in enumerate(bins['bin_0']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 150)), Unit(staff_bass.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        if toggle:
            num_func_map_1[best_order_1[int(idx / 2)]](staff_1, width, sus, sca, -2, inst)
            toggle = False
        else:
            num_func_map_2[best_order_2[int((idx - 1) / 2)]](staff_1, width, sus, sca, -2, inst)
            toggle = True
        cum = cum + (i - 1)

# Section 4 TSP
data = {'weights': (np.arange(1, 30)).tolist(),
        'values': (np.arange(2, 31)).tolist(),
        'bin capacities': [30, 30, 30]}
bins, bins_packed_value, bins_packed_weight = \
    multi_knapsack_mip(data['weights'], data['values'], data['bin capacities'])
print(bins)

num_func_map_1_pno = {
    0: draw_cell_1_1_pno,
    1: draw_cell_1_2_pno,
    2: draw_cell_1_3_pno,
    3: draw_cell_1_4_pno,
    4: draw_cell_1_5_pno,
    5: draw_cell_1_6_pno,
    6: draw_cell_1_7_pno,
    7: draw_cell_1_8_pno,
}

# Section 4 render cells
sca = "major_pentatonic"
if render_vln:
    cum = 0
    inst = "vln"
    for idx, i in enumerate(bins['bin_1'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 210)), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_1'])) - idx / len(bins['bin_1']))
        num_func_map_1[best_order_1[idx]](staff_1, width, sus, sca, 1, inst)
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    inst = "vc"
    for idx, i in enumerate(bins['bin_0'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 210)), Mm(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        num_func_map_1[best_order_1[idx]](staff_1, width, sus, sca, -1, inst)
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    inst = "pno"
    for idx, i in enumerate(bins['bin_2'][::-1]):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 210)), Mm(staff_treble.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        staff_1_b = Staff((Unit(zoom * (cum + 210)), Mm(staff_bass.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1_b, 'bass')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        num_func_map_1_pno[best_order_1[idx]](staff_1, staff_1_b, width, sus, sca, 0, inst)
        cum = cum + (i - 1)

# Section 5 render cells
sus = 0.5
sca = "major_pentatonic_g"
if render_vln:
    cum = 0
    inst = "vln"
    for idx, i in enumerate(bins['bin_2']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 240)), Unit(staff_vln.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_2'])) - idx / len(bins['bin_2']))
        if idx == 1 or idx == 0:
            num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, 1, inst)
        else:
            num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, 0, inst)
        cum = cum + (i - 1)

if render_vc:
    cum = 0
    sca = "major_pentatonic"
    inst = "vc"
    for idx, i in enumerate(bins['bin_1']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 240)), Mm(staff_vc.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'bass')
        sus = ((1 - 1 / len(bins['bin_1'])) - idx / len(bins['bin_1']))
        num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, -2, inst)
        cum = cum + (i - 1)

if render_pno:
    cum = 0
    inst = "pno"
    for idx, i in enumerate(bins['bin_0']):
        width = zoom * (i - 1)
        staff_1 = Staff((Unit(zoom * (cum + 240)), Mm(staff_treble.y)), parent=None, length=Unit(width))
        InvisibleClef(Unit(0), staff_1, 'treble')
        sus = ((1 - 1 / len(bins['bin_0'])) - idx / len(bins['bin_0']))
        num_func_map_2[best_order_2[idx]](staff_1, width, sus, sca, 1, inst)
        cum = cum + (i - 1)

# Full score mode: -30
# Pno mode: 59
# Vc mode: 14
# Vln mode: -22
# Strings mode: -22
for i in range(90 + 120 + 60):
    Text((Unit(zoom * i), Mm(59)), None, str(i))

prev_loc = 0
initial_x = 0
initial_y = 120
neoscore.set_viewport_center_pos((Unit(initial_x), Unit(initial_y)))
neoscore.set_viewport_scale(2.5)

neoscore.show(display_page_geometry=False)
start_time = time.time()
# neoscore.show(refresh_func, display_page_geometry=False)
fps = 60
duration = 285.0  # Duration of the video
video_from_rendered_images()
