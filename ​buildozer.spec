[app]
title = Calculator
package.name = calculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,pyjnius

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1

fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

# Android SDK / NDK setup
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
