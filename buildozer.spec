[app]
title = MizuEyeCare
package.name = mizueyecare
package.domain = org.mizu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,Cython==0.29.33
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, POST_NOTIFICATIONS

# ここが超重要！エラーを回避する固定設定
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.accept_sdk_license = True
android.skip_update = False
