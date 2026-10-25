@echo off
rem Local preview launcher for Windows.
rem   - prepends bin\win-shim so `convert` resolves to ImageMagick 7 (magick)
rem     instead of System32\convert.exe
rem   - layers _config.local.yml over _config.yml to skip the demo external
rem     post feeds and the Jupyter notebook (needs `jupyter` on PATH)
setlocal
cd /d "%~dp0.."
rem Also work in terminals opened before Ruby/ImageMagick were installed.
where ruby >nul 2>nul
if errorlevel 1 if exist "C:\Ruby34-x64\bin\ruby.exe" set "PATH=C:\Ruby34-x64\bin;%PATH%"
where node >nul 2>nul
if errorlevel 1 if exist "%ProgramFiles%\nodejs\node.exe" set "PATH=%ProgramFiles%\nodejs;%PATH%"
where magick >nul 2>nul
if errorlevel 1 for /d %%D in ("%ProgramFiles%\ImageMagick-*") do if exist "%%~D\magick.exe" set "PATH=%%~D;%PATH%"
set "PATH=%~dp0win-shim;%PATH%"
call bundle exec jekyll serve --config _config.yml,_config.local.yml --livereload %*
