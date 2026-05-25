# -*- mode: python ; coding: utf-8 -*-
import os
import playwright
from PyInstaller.utils.hooks import collect_all

# Obtenemos la ruta real de Playwright en tu venv
playwright_path = os.path.dirname(playwright.__file__)

# Recolectamos todas las dependencias automáticas
datas, binaries, hiddenimports = collect_all('playwright')

# --- TRUCO MAESTRO ---
# Forzamos la inclusión de los drivers y el ejecutable del navegador
datas += [
    (os.path.join(playwright_path, 'driver'), 'playwright/driver'),
]

block_cipher = None

a = Analysis(
    ['scraper.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SeeltyrScraper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SeeltyrScraper',
)