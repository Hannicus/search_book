# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

add_files = []



a = Analysis(['main.py','network_book.py','published_book.py','result_analyse.py','search.py','UI.py','unvisable_avoiddetection.py'],
             pathex=['D:\\pythonProject1\\search_book'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='search_book',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='D:\\pythonProject1\\search_book\\axy7l-2y9zl-001.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
