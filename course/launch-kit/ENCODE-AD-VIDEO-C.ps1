# Encode Creative C (30s, 900 frames) from the numbered frame sequence.
# Put this file NEXT TO the ad-frames-c folder, then run it.

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".\ad-frames-c")) {
    Write-Host "ERROR: no ad-frames-c folder here. Put this script next to it." -ForegroundColor Red
    exit 1
}

$count = (Get-ChildItem ".\ad-frames-c\*.png").Count
Write-Host "Found $count frames." -ForegroundColor Cyan

ffmpeg -y -framerate 30 -i ".\ad-frames-c\f%05d.png" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "ad-creative-c.mp4"

if (Test-Path "ad-creative-c.mp4") {
    $kb = (Get-Item "ad-creative-c.mp4").Length / 1KB
    Write-Host ("Done: ad-creative-c.mp4  {0:N0} KB  - 1080x1920, 30s, silent" -f $kb) -ForegroundColor Green
} else {
    Write-Host "Encoding failed. Copy the ffmpeg output above." -ForegroundColor Red
}
