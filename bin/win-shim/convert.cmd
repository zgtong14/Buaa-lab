@echo off
rem Shim: jekyll-imagemagick invokes the bare `convert`, which on Windows hits
rem System32\convert.exe (the FAT->NTFS tool). ImageMagick 7 ships `magick`
rem instead of the legacy `convert`, so forward to it. Put this dir ahead of
rem System32 on PATH before running jekyll.
magick %*
