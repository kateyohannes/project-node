import subprocess

from ffmpeg import FFmpeg, Progress


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("assets/video/sample.mp4")
        .input("assets/video/sample_2.mp4")
        .output(
            "asset/video/output/out.mp4",
            map=["0:0", "1:1"],
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute()


if __name__ == "__main__":
    main()
