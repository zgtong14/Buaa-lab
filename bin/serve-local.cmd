@echo off
rem Local preview launcher for Windows.
rem   - prepends bin\win-shim so `convert` resolves to ImageMagick 7 (magick)
rem     instead of System32\convert.exe
rem   - layers _config.local.yml over _config.yml to skip the demo external
rem     post feeds and the Jupyter notebook (needs `jupyter` on PATH)
setlocal
cd /d "%~dp0.."
set "PATH=%~dp0win-shim;%PATH%"
bundle exec jekyll serve --config _config.yml,_config.local.yml --livereload %*
