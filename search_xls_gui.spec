# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['search_xls_gui.py','src\\utils.py','src\\ui\\ui_main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['src.*','src.ui.*'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['faker','pyinstaller'],
    noarchive=True,  # 修改此处
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='search_xls_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resource\\search.ico'],
    onefile=False,  # 添加此行
)
