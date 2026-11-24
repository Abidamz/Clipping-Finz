# Encode Creative B (28s, 840 frames) from the numbered frame sequence.
# Put this file NEXT TO the ad-frames-b folder, then run it.

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".\ad-frames-b")) {
    Write-Host "ERROR: no ad-frames-b folder here. Put this script next to it." -ForegroundColor Red
    exit 1
}

$count = (Get-ChildItem ".\ad-frames-b\*.png").Count
Write-Host "Found $count frames." -ForegroundColor Cyan

ffmpeg -y -framerate 30 -i ".\ad-frames-b\f%05d.png" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "ad-creative-b.mp4"

if (Test-Path "ad-creative-b.mp4") {
    $kb = (Get-Item "ad-creative-b.mp4").Length / 1KB
    Write-Host ("Done: ad-creative-b.mp4  {0:N0} KB  - 1080x1920, 28s, silent" -f $kb) -ForegroundColor Green
} else {
    Write-Host "Encoding failed. Copy the ffmpeg output above." -ForegroundColor Red
}
