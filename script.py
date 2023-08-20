from ffmpeg import FFmpeg


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("assets/video/sample.mp4")
        .output(
            "ouptut.mp4",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()
