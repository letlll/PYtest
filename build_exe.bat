@echo off
echo ===== 创建Python可执行文件 =====
echo.

REM 检查是否安装了PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo PyInstaller安装失败！
        echo 请确保已安装Python并添加到PATH环境变量。
        pause
        exit /b 1
    )
)

echo.
echo 选择创建方式:
echo 1. 创建控制台应用程序 (显示命令行窗口)
echo 2. 创建窗口应用程序 (不显示命令行窗口，推荐)
echo.

set /p choice="请输入选择 (1 或 2): "

if "%choice%"=="1" (
    echo.
    echo 正在创建控制台应用程序...
    pyinstaller --onefile main.py
) else if "%choice%"=="2" (
    echo.
    echo 正在创建窗口应用程序...
    pyinstaller --onefile --noconsole main.py
) else (
    echo.
    echo 无效的选择！
    pause
    exit /b 1
)

if %errorlevel% neq 0 (
    echo.
    echo 创建失败！
    pause
    exit /b 1
)

echo.
echo 创建成功！可执行文件位于 dist 目录中。
echo.

explorer dist
pause 