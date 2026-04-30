[app]
title = MizuEyeCare
package.name = mizueyecare
package.domain = org.mizu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, POST_NOTIFICATIONS

# ここから下が大事な追加設定！
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.skip_update = False
android.accept_sdk_license = True
