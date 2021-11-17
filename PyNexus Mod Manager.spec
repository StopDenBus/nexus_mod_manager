# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['app\\__init__.py'],
             pathex=['C:/Meine_Programme/python3.10/Lib/site-packages', 'C:/Users/micha/AppData/Local/pypoetry/Cache/virtualenvs/nexus-mod-manager-j0_7xe9s-py3.10/Lib/site-packages', 'C:/Meine_Programme/python3.10/Lib/site-packages/PyQt6/Qt6/bin', 'C:/git/nexus_mod_manager/app'],
             binaries=[],
             datas=[('C:/Users/micha/AppData/Local/pypoetry/Cache/virtualenvs/nexus-mod-manager-j0_7xe9s-py3.10/Lib/site-packages/PyQt6/Qt6/plugins/platforms', 'platforms/')],
             hiddenimports=['PyQt6', 'cryptography' ],
             hookspath=['.\\hooks\\'],
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
          [],
          exclude_binaries=True,
          name='PyNexus Mod Manager',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PyNexus Mod Manager')
