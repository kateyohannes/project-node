import asyncio

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("assets/video/sample.mp4")
        .output(
            "assets/video/out/ouptut.avi",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="slow",
            crf=24,
        )
    )

    await ffmpeg.execute()


if __name__ == "__main__":
    asyncio.run(main())
