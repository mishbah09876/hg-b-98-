[app]
# Basic app metadata
title = ShadeX-Ai
package.name = shadex_ai
package.domain = org.example.shadex_ai

# Where your source lives
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Dependencies the APK needs
requirements = python3,kivy,pyjnius,android

# Android settings
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.arch = arm64-v8a
android.enable_androidx = True

icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# Increase verbosity to capture full logs in CI
log_level = 2
