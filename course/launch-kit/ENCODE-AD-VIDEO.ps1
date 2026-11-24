# Encode the TikTok ad video from the numbered frame sequence.
# Put this file in the same folder as the `ad-frames` folder, then:
#   Right-click -> Run with PowerShell
#   (or)  powershell -ExecutionPolicy Bypass -File .\ENCODE-AD-VIDEO.ps1

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".\ad-frames")) {
    Write-Host "ERROR: no ad-frames folder here. Put this script next to it." -ForegroundColor Red
    exit 1
}

$count = (Get-ChildItem ".\ad-frames\*.png").Count
Write-Host "Found $count frames ($([math]::Round($count/30,1)) seconds at 30fps)." -ForegroundColor Cyan

ffmpeg -y -framerate 30 -i ".\ad-frames\f%05d.png" `
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p `
  -movflags +faststart "ad-creative-a.mp4"

if (Test-Path "ad-creative-a.mp4") {
    $mb = (Get-Item "ad-creative-a.mp4").Length / 1MB
    Write-Host ("Done: ad-creative-a.mp4  {0:N1} MB  - 1080x1920, 24s, silent" -f $mb) -ForegroundColor Green
    Write-Host "Upload this as the ad video in TikTok Ads Manager." -ForegroundColor Green
} else {
    Write-Host "Encoding failed - copy the ffmpeg output above and send it to me." -ForegroundColor Red
}
