from neoscore.common import *
from neoscore.western.notehead_tables import NoteheadTable
import numpy as np


def map_to_scale(scale, degree, octave=0):
    def octave_up(n):
        if n[-1] == "'":
            n += "'"
        elif n[-1] == ",":
            n = n[:-1]
        else:
            n += "'"
        return n

    def octave_down(n):
        if n[-1] == "'":
            n = n[:-1]
        elif n[-1] == ",":
            n += ","
        else:
            n += ","
        return n

    match scale:
        case 'chromatic_c':
            mapping = {
                0: 'cn',
                1: 'cs',
                2: 'dn',
                3: 'ds',
                4: 'en',
                5: 'fn',
                6: 'fs',
                7: 'gn',
                8: 'gs',
                9: 'an',
                10: 'as',
                11: 'bn'
            }
            note = mapping[degree]
        case 'major_pentatonic':
            mapping = {
                0: 'c',
                1: 'd',
                2: 'e',
                3: 'g',
                4: 'a',
                5: "c'",
                6: "d'",
                7: "e'",
                8: "g'",
                9: "a'"
            }
            note = mapping[degree]
        case 'major_pentatonic_g':
            mapping = {
                0: 'g,',
                1: 'a,',
                2: 'c',
                3: 'd',
                4: 'e',
                5: "g",
                6: "a",
                7: "c'",
                8: "d'",
                9: "e'"
            }
            note = mapping[degree]
        case 'minor_pentatonic':
            mapping = {
                0: 'c',
                1: 'd',
                2: 'f',
                3: 'g',
                4: 'a',
                5: "c'",
                6: "d'"
            }
            note = mapping[degree]
        case 'ionian':
            mapping = {
                0: 'c',
                1: 'd',
                2: 'e',
                3: 'f',
                4: 'g',
                5: 'a',
                6: 'b'
            }
            note = mapping[degree]
        case 'aeolean':
            mapping = {
                0: 'c',
                1: 'd',
                2: 'eb',
                3: 'f',
                4: 'g',
                5: 'ab',
                6: 'bb'
            }
            note = mapping[degree]
        case 'octatonic[0,1]':
            mapping = {
                0: 'cn',
                1: 'cs',
                2: 'ds',
                3: 'en',
                4: 'fs',
                5: 'gn',
                6: 'gs',
                7: 'as'
            }
            note = mapping[degree]
        case 'hexatonic[0,1]':
            mapping = {
                0: 'c',
                1: 'db',
                2: 'e',
                3: 'f',
                4: 'gs',
                5: 'a',
                6: "c'",
                7: "db'"
            }
            note = mapping[degree]
        case other:
            print("Not a valid scale")
    if octave > 0:
        for i in range(octave):
            note = octave_up(note)
    elif octave < 0:
        for i in range(abs(octave)):
            note = octave_down(note)
    return note


def cap_sustain(sustain, cell_width):
    if sustain > 0.7 and cell_width < 200:
        sustain = 0.7
    return sustain


def draw_cell_1_1(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    if cell_width > 200 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_1_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave),
                                                   map_to_scale(scale, 2, octave),
                                                   map_to_scale(scale, 3, octave)], (1, 4), table=table)
    n1_b = Chordrest(Unit(cell_width * 0.0), staff_b, [map_to_scale(scale, 1, octave-2),
                                                       map_to_scale(scale, 5, octave-2)], (1, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave),
                                                    map_to_scale(scale, 1, octave),
                                                    map_to_scale(scale, 2, octave)], (1, 4), table=table)
    n2_b = Chordrest(Unit(cell_width * 0.25), staff_b, [map_to_scale(scale, 0, octave-2),
                                                        map_to_scale(scale, 3, octave-2)], (1, 4), table=table)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave),
                                                   map_to_scale(scale, 4, octave),
                                                   map_to_scale(scale, 5, octave)], (1, 4), table=table)
    n3_b = Chordrest(Unit(cell_width * 0.5), staff_b, [map_to_scale(scale, 3, octave-2),
                                                       map_to_scale(scale, 5, octave-2)], (1, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave),
                                                    map_to_scale(scale, 4, octave),
                                                    map_to_scale(scale, 6, octave)], (1, 4), table=table)
    n4_b = Chordrest(Unit(cell_width * 0.75), staff_b, [map_to_scale(scale, 2, octave-2),
                                                        map_to_scale(scale, 4, octave-2)], (1, 4), table=table)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_2(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n1 = Chordrest(Unit(cell_width * 0.125), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    MusicText(n1.extra_attachment_point, n1, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.375), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    MusicText(n2.extra_attachment_point, n2, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.625), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    MusicText(n3.extra_attachment_point, n3, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.875), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    MusicText(n4.extra_attachment_point, n4, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_2_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n1 = Chordrest(Unit(cell_width * 0.125), staff_b, [map_to_scale(scale, 1, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.375), staff_b, [map_to_scale(scale, 0, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.625), staff_b, [map_to_scale(scale, 3, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.875), staff_b, [map_to_scale(scale, 2, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.124 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_3(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.16 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.42), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.07 * sustain), Unit(0)), pen=pen)
    MusicText(n3.extra_attachment_point, n3, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n4 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    if cell_width > 200 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-7)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-6)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n5.x, staff.unit(-6)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_3_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave),
                                                   map_to_scale(scale, 3, octave),
                                                   map_to_scale(scale, 5, octave)], (1, 4), table=table)
    n1 = Chordrest(Unit(cell_width * 0.0), staff_b, [map_to_scale(scale, 1, octave-1),
                                                     map_to_scale(scale, 4, octave-1)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave),
                                                    map_to_scale(scale, 2, octave),
                                                    map_to_scale(scale, 4, octave)], (1, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.25), staff_b, [map_to_scale(scale, 0, octave-1),
                                                      map_to_scale(scale, 3, octave-1)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.16 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.42), staff, [map_to_scale(scale, 5, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.07 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 3, octave),
                                                   map_to_scale(scale, 5, octave),
                                                   map_to_scale(scale, 7, octave)], (1, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.5), staff_b, [map_to_scale(scale, 3, octave-1),
                                                     map_to_scale(scale, 6, octave-1)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 2, octave),
                                                    map_to_scale(scale, 4, octave),
                                                    map_to_scale(scale, 6, octave)], (1, 4), table=table)
    n5 = Chordrest(Unit(cell_width * 0.75), staff_b, [map_to_scale(scale, 2, octave-1),
                                                      map_to_scale(scale, 5, octave-1)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_4(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.2), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.4), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.07 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.88), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_4_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave),
                                                   map_to_scale(scale, 2, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.2), staff, [map_to_scale(scale, 0, octave),
                                                   map_to_scale(scale, 1, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.4), staff, [map_to_scale(scale, 5, octave),
                                                   map_to_scale(scale, 6, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 3, octave),
                                                   map_to_scale(scale, 4, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.19 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 1, octave),
                                                   map_to_scale(scale, 2, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.07 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.88), staff, [map_to_scale(scale, 2, octave)], (1, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_5(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    MusicText(n1.extra_attachment_point, n1, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n2 = Chordrest(Unit(cell_width * 0.05), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.1), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.14 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    MusicText(n4.extra_attachment_point, n4, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n5 = Chordrest(Unit(cell_width * 0.3), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.35), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.14 * sustain), Unit(0)), pen=pen)
    n7 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n7.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    MusicText(n7.extra_attachment_point, n7, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n8 = Chordrest(Unit(cell_width * 0.55), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n8.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    n9 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n9.noteheads[0], (Unit(cell_width * 0.14 * sustain), Unit(0)), pen=pen)
    n10 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n10.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    MusicText(n10.extra_attachment_point, n10, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n11 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n11.noteheads[0], (Unit(cell_width * 0.04 * sustain), Unit(0)), pen=pen)
    n12 = Chordrest(Unit(cell_width * 0.85), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n12.noteheads[0], (Unit(cell_width * 0.14 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_5_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    n1_b = Chordrest(Unit(cell_width * 0.0), staff_b, [map_to_scale(scale, 3, octave-1)], (4, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.05), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n2_b = Chordrest(Unit(cell_width * 0.05), staff_b, [map_to_scale(scale, 2, octave-1)], (4, 4), table=table)
    n3 = Chordrest(Unit(cell_width * 0.1), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n3_b = Chordrest(Unit(cell_width * 0.1), staff_b, [map_to_scale(scale, 1, octave-1)], (4, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n4_b = Chordrest(Unit(cell_width * 0.25), staff_b, [map_to_scale(scale, 2, octave-1)], (4, 4), table=table)
    n5 = Chordrest(Unit(cell_width * 0.3), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n5_b = Chordrest(Unit(cell_width * 0.3), staff_b, [map_to_scale(scale, 1, octave-1)], (4, 4), table=table)
    n6 = Chordrest(Unit(cell_width * 0.35), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    n6_b = Chordrest(Unit(cell_width * 0.35), staff_b, [map_to_scale(scale, 0, octave-1)], (4, 4), table=table)
    n7 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    n7_b = Chordrest(Unit(cell_width * 0.5), staff_b, [map_to_scale(scale, 5, octave-1)], (4, 4), table=table)
    n8 = Chordrest(Unit(cell_width * 0.55), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    n8_b = Chordrest(Unit(cell_width * 0.55), staff_b, [map_to_scale(scale, 4, octave-1)], (4, 4), table=table)
    n9 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    n9_b = Chordrest(Unit(cell_width * 0.6), staff_b, [map_to_scale(scale, 3, octave-1)], (4, 4), table=table)
    n10 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    n10_b = Chordrest(Unit(cell_width * 0.75), staff_b, [map_to_scale(scale, 0, octave-1)], (4, 4), table=table)
    n11 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n11_b = Chordrest(Unit(cell_width * 0.8), staff_b, [map_to_scale(scale, 1, octave-1)], (4, 4), table=table)
    n12 = Chordrest(Unit(cell_width * 0.85), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n12_b = Chordrest(Unit(cell_width * 0.85), staff_b, [map_to_scale(scale, 2, octave-1)], (4, 4), table=table)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_6(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.125), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.375), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.625), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n7 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n7.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n8 = Chordrest(Unit(cell_width * 0.875), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n8.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_6_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.125), staff_b, [map_to_scale(scale, 1, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.375), staff_b, [map_to_scale(scale, 3, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.625), staff_b, [map_to_scale(scale, 0, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n7 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n7.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)
    n8 = Chordrest(Unit(cell_width * 0.875), staff_b, [map_to_scale(scale, 2, octave-1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n8.noteheads[0], (Unit(cell_width * 0.115 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_7(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 6, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    MusicText(n3.extra_attachment_point, n3, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    if cell_width > 200 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-8)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-7)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_7_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave),
                                                   map_to_scale(scale, 4, octave),
                                                   map_to_scale(scale, 6, octave)], (1, 4), table=table)
    n1_b = Chordrest(Unit(cell_width * 0.0), staff_b, [map_to_scale(scale, 2, octave-2),
                                                       map_to_scale(scale, 6, octave-2)], (1, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 0, octave),
                                                    map_to_scale(scale, 2, octave),
                                                    map_to_scale(scale, 4, octave)], (1, 4), table=table)
    n2_b = Chordrest(Unit(cell_width * 0.25), staff_b, [map_to_scale(scale, 0, octave-2),
                                                        map_to_scale(scale, 4, octave-2)], (1, 4), table=table)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 6, octave),
                                                   map_to_scale(scale, 8, octave),
                                                   map_to_scale(scale, 2, octave)], (1, 4), table=table)
    n3_b = Chordrest(Unit(cell_width * 0.5), staff_b, [map_to_scale(scale, 6, octave-2),
                                                       map_to_scale(scale, 3, octave-1)], (1, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 4, octave),
                                                    map_to_scale(scale, 6, octave),
                                                    map_to_scale(scale, 8, octave)], (1, 4), table=table)
    n4_b = Chordrest(Unit(cell_width * 0.75), staff_b, [map_to_scale(scale, 4, octave-2),
                                                        map_to_scale(scale, 3, octave-1)], (1, 4), table=table)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_8(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.1), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.2), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.3), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.69 * sustain), Unit(0)), pen=pen)
    MusicText(n4.extra_attachment_point, n1, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if cell_width > 200 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n4.x, staff.unit(-5)), staff, "vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_1_8_pno(staff, staff_b, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.1), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    n3 = Chordrest(Unit(cell_width * 0.2), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.3), staff, [map_to_scale(scale, 2, octave),
                                                   map_to_scale(scale, 0, octave)], (4, 4), table=table)
    n4_b = Chordrest(Unit(cell_width * 0.3), staff_b, [map_to_scale(scale, 2, octave-1),
                                                       map_to_scale(scale, 0, octave-1),
                                                       map_to_scale(scale, 4, octave-1)
                                                       ], (4, 4), table=table)
    for i in n4.noteheads:
        Path.straight_line((Unit(3), Unit(0)), i, (Unit(cell_width * 0.69 * sustain), Unit(0)), pen=pen)
    for i in n4_b.noteheads:
        Path.straight_line((Unit(3), Unit(0)), i, (Unit(cell_width * 0.69 * sustain), Unit(0)), pen=pen)

    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_1(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_2(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.24 * sustain), Unit(0)), pen=pen)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_3(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 3, octave+1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.125), staff, [map_to_scale(scale, 4, octave+1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.375), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 4, octave + 1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    MusicText(n5.extra_attachment_point, n5, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n6 = Chordrest(Unit(cell_width * 0.625), staff, [map_to_scale(scale, 5, octave + 1)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    MusicText(n6.extra_attachment_point, n6, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n7 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n7.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n8 = Chordrest(Unit(cell_width * 0.875), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n8.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n5.tremolo_attachment_point, n5, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n7.tremolo_attachment_point, n7, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n5.x, staff.unit(-7)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n7.x, staff.unit(-6)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_4(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n1.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n2 = Chordrest(Unit(cell_width * 0.125), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n2.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n3 = Chordrest(Unit(cell_width * 0.25), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.375), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.625), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n7 = Chordrest(Unit(cell_width * 0.75), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n7.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    n8 = Chordrest(Unit(cell_width * 0.875), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n8.noteheads[0], (Unit(cell_width * 0.11 * sustain), Unit(0)), pen=pen)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n6.tremolo_attachment_point, n6, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n8.tremolo_attachment_point, n8, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n6.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n8.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_5(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.45), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n1.highest_notehead,
                           (staff.unit(0), ZERO), n2.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.95), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n3.highest_notehead,
                           (staff.unit(0), ZERO), n4.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_6(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    MusicText(n1.extra_attachment_point, n1, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n2 = Chordrest(Unit(cell_width * 0.2), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n1.highest_notehead,
                           (staff.unit(0), ZERO), n2.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    MusicText(n2.extra_attachment_point, n2, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n3 = Chordrest(Unit(cell_width * 0.3), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n3.highest_notehead,
                           (staff.unit(0), ZERO), n4.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    n5 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    MusicText(n5.extra_attachment_point, n5, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n6 = Chordrest(Unit(cell_width * 0.7), staff, [map_to_scale(scale, 5, octave)], (4, 4), table=table)
    MusicText(n6.extra_attachment_point, n6, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n5.highest_notehead,
                           (staff.unit(0), ZERO), n6.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    n7 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    n8 = Chordrest(Unit(cell_width * 0.9), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n7.highest_notehead,
                           (staff.unit(0), ZERO), n8.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n5.tremolo_attachment_point, n5, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n7.tremolo_attachment_point, n7, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n5.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n7.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_7(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 2, octave)], (4, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.4), staff, [map_to_scale(scale, 7, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n1.highest_notehead,
                           (staff.unit(0), ZERO), n2.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    MusicText(n2.extra_attachment_point, n2, "articAccentBelow",
              alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n3.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n4 = Chordrest(Unit(cell_width * 0.6), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n4.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n5 = Chordrest(Unit(cell_width * 0.7), staff, [map_to_scale(scale, 1, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n5.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    n6 = Chordrest(Unit(cell_width * 0.8), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    Path.straight_line((Unit(3), Unit(0)), n6.noteheads[0], (Unit(cell_width * 0.09 * sustain), Unit(0)), pen=pen)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n5.tremolo_attachment_point, n5, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n6.tremolo_attachment_point, n6, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n5.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n6.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    Barline(Unit(cell_width * 1 - 6), staff.group)


def draw_cell_2_8(staff, cell_width, sustain, scale, octave=0, instrument=None):
    sustain = cap_sustain(sustain, cell_width)
    table = NoteheadTable(double_whole='noteheadBlack', whole='noteheadBlack',
                          half='noteheadBlack', short='noteheadBlack')
    pen = Pen(thickness=Mm(1.1))
    n1 = Chordrest(Unit(cell_width * 0.0), staff, [map_to_scale(scale, 3, octave)], (4, 4), table=table)
    n2 = Chordrest(Unit(cell_width * 0.45), staff, [map_to_scale(scale, 7, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n1.highest_notehead,
                           (staff.unit(0), ZERO), n2.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    n3 = Chordrest(Unit(cell_width * 0.5), staff, [map_to_scale(scale, 4, octave)], (4, 4), table=table)
    n4 = Chordrest(Unit(cell_width * 0.95), staff, [map_to_scale(scale, 0, octave)], (4, 4), table=table)
    RepeatingMusicTextLine((staff.unit(2), ZERO), n3.highest_notehead,
                           (staff.unit(0), ZERO), n4.highest_notehead,
                           "wiggleGlissando", None, "wiggleArpeggiatoUpArrow")
    Barline(Unit(cell_width * 1 - 6), staff.group)
    if cell_width > 500 and sustain > 0.55:
        MusicText(n1.tremolo_attachment_point, n1, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n2.tremolo_attachment_point, n2, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n3.tremolo_attachment_point, n3, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
        MusicText(n4.tremolo_attachment_point, n4, "tremolo3",
                  alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
    if 300 < cell_width < 500 and sustain > 0.4:
        if instrument == "vln" or instrument == "vc":
            Text((n1.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n2.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n3.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)
            Text((n4.x, staff.unit(-5)), staff, "molto vib.", neoscore.default_font.modified(italic=True),
                 alignment_x=AlignmentX.CENTER, alignment_y=AlignmentY.CENTER)

if __name__ == '__main__':
    neoscore.setup()

    neoscore.document.pages[1]

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

    coord = coord * 500
    width = 200
    sus = 0.5
    oc = 2
    inst = "vln"
    sca = "chromatic_c"
    staff_1 = Staff((Unit(coord[0][0]), Unit(coord[0][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_1, 'treble')
    draw_cell_1_1(staff_1, width, sus, sca, oc, inst)

    staff_2 = Staff((Unit(coord[1][0]), Unit(coord[1][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_2, 'treble')
    draw_cell_1_2(staff_2, width, sus, sca, oc)

    staff_3 = Staff((Unit(coord[2][0]), Unit(coord[2][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_3, 'treble')
    draw_cell_1_3(staff_3, width, sus, sca, oc)

    staff_4 = Staff((Unit(coord[3][0]), Unit(coord[3][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_4, 'treble')
    draw_cell_1_4(staff_4, width, sus, sca, oc)

    staff_5 = Staff((Unit(coord[4][0]), Unit(coord[4][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_5, 'treble')
    draw_cell_1_5(staff_5, width, sus, sca, oc)

    staff_6 = Staff((Unit(coord[5][0]), Unit(coord[5][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_6, 'treble')
    draw_cell_1_6(staff_6, width, sus, sca, oc)

    staff_7 = Staff((Unit(coord[6][0]), Unit(coord[6][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_7, 'treble')
    draw_cell_1_7(staff_7, width, sus, sca, oc)

    staff_8 = Staff((Unit(coord[7][0]), Unit(coord[7][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_8, 'treble')
    draw_cell_1_8(staff_8, width, sus, sca, oc)

    # character - complexity space
    off = -2.5
    coord = np.array([
        [0+off, 0],
        [0.3+off, 0.4],
        [0.2+off, 0.2],
        [0.4+off, 0.3],
        [0.8+off, 1],
        [0.5+off, 0.8],
        [0.1+off, 0.1],
        [1+off, 0.1]
    ])

    coord = coord * 500
    width = 200
    sus = 0.5
    oc = 0
    sca = "major_pentatonic"
    staff_1 = Staff((Unit(coord[0][0]), Unit(coord[0][1])), parent=None, length=Unit(width))
    staff_1_b = Staff((Unit(coord[0][0]), Unit(coord[0][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_1, 'treble')
    InvisibleClef(Unit(0), staff_1_b, 'bass')
    draw_cell_1_1_pno(staff_1, staff_1_b, width, sus, sca, oc)

    staff_2 = Staff((Unit(coord[1][0]), Unit(coord[1][1])), parent=None, length=Unit(width))
    staff_2_b = Staff((Unit(coord[1][0]), Unit(coord[1][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_2, 'treble')
    InvisibleClef(Unit(0), staff_2_b, 'bass')
    draw_cell_1_2_pno(staff_2, staff_2_b, width, sus, sca, oc)

    staff_3 = Staff((Unit(coord[2][0]), Unit(coord[2][1])), parent=None, length=Unit(width))
    staff_3_b = Staff((Unit(coord[2][0]), Unit(coord[2][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_3, 'treble')
    InvisibleClef(Unit(0), staff_3_b, 'bass')
    draw_cell_1_3_pno(staff_3, staff_3_b, width, sus, sca, oc)

    staff_4 = Staff((Unit(coord[3][0]), Unit(coord[3][1])), parent=None, length=Unit(width))
    staff_4_b = Staff((Unit(coord[3][0]), Unit(coord[3][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_4, 'treble')
    InvisibleClef(Unit(0), staff_4_b, 'bass')
    draw_cell_1_4_pno(staff_4, staff_4_b, width, sus, sca, oc)

    staff_5 = Staff((Unit(coord[4][0]), Unit(coord[4][1])), parent=None, length=Unit(width))
    staff_5_b = Staff((Unit(coord[4][0]), Unit(coord[4][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_5, 'treble')
    InvisibleClef(Unit(0), staff_5_b, 'bass')
    draw_cell_1_5_pno(staff_5, staff_5_b, width, sus, sca, oc)

    staff_6 = Staff((Unit(coord[5][0]), Unit(coord[5][1])), parent=None, length=Unit(width))
    staff_6_b = Staff((Unit(coord[5][0]), Unit(coord[5][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_6, 'treble')
    InvisibleClef(Unit(0), staff_6_b, 'bass')
    draw_cell_1_6_pno(staff_6, staff_6_b, width, sus, sca, oc)

    staff_7 = Staff((Unit(coord[6][0]), Unit(coord[6][1])), parent=None, length=Unit(width))
    staff_7_b = Staff((Unit(coord[6][0]), Unit(coord[6][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_7, 'treble')
    InvisibleClef(Unit(0), staff_7_b, 'bass')
    draw_cell_1_7_pno(staff_7, staff_7_b, width, sus, sca, oc)

    staff_8 = Staff((Unit(coord[7][0]), Unit(coord[7][1])), parent=None, length=Unit(width))
    staff_8_b = Staff((Unit(coord[7][0]), Unit(coord[7][1] + 50)), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_8, 'treble')
    InvisibleClef(Unit(0), staff_8_b, 'bass')
    draw_cell_1_8_pno(staff_8, staff_8_b, width, sus, sca, oc)

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

    coord = coord * 500
    width = 200
    sus = 0.5
    oc = 1
    inst = "vln"
    sca = "octatonic[0,1]"
    staff_1 = Staff((Unit(coord[0][0]), Unit(coord[0][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_1, 'treble')
    draw_cell_2_1(staff_1, width, sus, sca, oc)

    staff_2 = Staff((Unit(coord[1][0]), Unit(coord[1][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_2, 'treble')
    draw_cell_2_2(staff_2, width, sus, sca, oc)

    staff_3 = Staff((Unit(coord[2][0]), Unit(coord[2][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_3, 'treble')
    draw_cell_2_3(staff_3, width, sus, sca, oc)

    staff_4 = Staff((Unit(coord[3][0]), Unit(coord[3][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_4, 'treble')
    draw_cell_2_4(staff_4, width, sus, sca, oc)

    staff_5 = Staff((Unit(coord[4][0]), Unit(coord[4][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_5, 'treble')
    draw_cell_2_5(staff_5, width, sus, sca, oc)

    staff_6 = Staff((Unit(coord[5][0]), Unit(coord[5][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_6, 'treble')
    draw_cell_2_6(staff_6, width, sus, sca, oc)

    staff_7 = Staff((Unit(coord[6][0]), Unit(coord[6][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_7, 'treble')
    draw_cell_2_7(staff_7, width, sus, sca, oc)

    staff_8 = Staff((Unit(coord[7][0]), Unit(coord[7][1])), parent=None, length=Unit(width))
    InvisibleClef(Unit(0), staff_8, 'treble')
    draw_cell_2_8(staff_8, width, sus, sca, oc)

    neoscore.show()
