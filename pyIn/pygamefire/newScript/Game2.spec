# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Game2.py'],
             pathex=['/Users/neilleonard/Desktop/Coding/exeDev/pyIn/pygamefire/newScript'],
             binaries=[],
             datas=[('*.tsx','.'),('tmx.py','.'),('*.tmx','.'),('classes/*','classes/'),('fonts/*','fonts/'),('images/*','images/'),('sounds/*','sounds/'),('sprites/*','sprites/'),('tiles/*','tiles/')],
             hiddenimports=[],
             hookspath=[],
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
          [],
          exclude_binaries=True,
          name='Game2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Game2')
