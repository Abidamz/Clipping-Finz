# Encode Creative D (22s, 660 frames) from the numbered frame sequence.
# Put this file NEXT TO the ad-frames-d folder, then run it.

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".\ad-frames-d")) {
    Write-Host "ERROR: no ad-frames-d folder here. Put this script next to it." -ForegroundColor Red
    exit 1
}

$count = (Get-ChildItem ".\ad-frames-d\*.png").Count
Write-Host "Found $count frames." -ForegroundColor Cyan

ffmpeg -y -framerate 30 -i ".\ad-frames-d\f%05d.png" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "ad-creative-d.mp4"

if (Test-Path "ad-creative-d.mp4") {
    $kb = (Get-Item "ad-creative-d.mp4").Length / 1KB
    Write-Host ("Done: ad-creative-d.mp4  {0:N0} KB  - 1080x1920, 22s, silent" -f $kb) -ForegroundColor Green
} else {
    Write-Host "Encoding failed. Copy the ffmpeg output above." -ForegroundColor Red
}
