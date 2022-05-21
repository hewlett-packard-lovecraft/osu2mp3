import unittest
import time
import os

from pathlib import Path
from osu2mp3.app import app
from osu2mp3.progressbar import progressbar
from osu2mp3.beatmap import beatmap


def make_orderer():
    order = {}

    def ordered(f):
        order[f.__name__] = len(order)
        return f

    def compare(a, b):
        return [1, -1][order[a] < order[b]]

    return ordered, compare


ordered, compare = make_orderer()
unittest.defaultTestLoader.sortTestMethodsUsing = compare


class TestOsu2mp3(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """ set up classess """
        cls.app = app.App(Path("input_dir"), Path("output_dir"))
        cls.beatmap = beatmap.Beatmap(Path("input_dir"), Path("output_dir"))


    @ordered
    def test_adjust_pb_size(self):
        terminal_width = os.get_terminal_size().columns
        self.app.adjust_pb_size()

        self.assertTrue(self.app.disp_length < terminal_width)

        if terminal_width > 150:
            self.assertEqual(self.app.bar_width, 80)
        else:
            self.assertEqual(self.app.bar_width, 60)


    @ordered
    def test_progressbar(self):
        """ test the progressbar """
        total_steps = 12
        bar_width, disp_len = self.app.adjust_pb_size()
        print(f"progressbar length: {disp_len}")
        print(f"progressbar bar width: {bar_width}")

        for step in range(0, total_steps):
            progressbar.progressbar(
                step=step+1, total=total_steps, title="Testing progressbar", bar_width=bar_width, disp_len=disp_len)

            time.sleep(0.1)

    @ordered
    def test_regex(self):
        self.beatmap.tags_file = """
            osu file format v14

            [General]
            AudioFilename: audio.mp3
            AudioLeadIn: 0
            PreviewTime: 74965
            Countdown: 0
            SampleSet: Soft
            StackLeniency: 0.4
            Mode: 0
            LetterboxInBreaks: 0
            WidescreenStoryboard: 1

            [Editor]
            Bookmarks: 75170,101700,200038,205753,205957,206161,206365,206569,206977,207181,207385,207794,207998,208202
            DistanceSpacing: 1
            BeatDivisor: 4
            GridSize: 8
            TimelineZoom: 1.8

            [Metadata]
            Title:Song Title
            Artist:Song Artist
            Creator:
            Version:
            Source:Song Source
            Tags:tag1 tag2 tag3 tag4
            BeatmapID:2817456
            BeatmapSetID:1313664
            """
        self.beatmap.read_tags()

        print("\n")
        print(f"audiofile_name: {self.beatmap.audiofile_name}")
        print(f"title: {self.beatmap.title}")
        print(f"artist: {self.beatmap.artist}")
        print(f"song source: {self.beatmap.album_name}")
        print(f"song genres: {self.beatmap.song_genre}")

        self.assertEqual(self.beatmap.audiofile_name, "audio.mp3")
        self.assertEqual(self.beatmap.title, "Song Title")
        self.assertEqual(self.beatmap.artist, "Song Artist")
        self.assertEqual(self.beatmap.album_name, "Song Source")
        self.assertEqual(self.beatmap.song_genre, ["tag1", "tag2", "tag3", "tag4"])


if __name__ == '__main__':
    unittest.main()
