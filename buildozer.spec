[app]
# Basic app metadata
title = WebViewApp
package.name = webviewapp
package.domain = org.example

# Where your source lives
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Dependencies the APK needs
requirements = python3,kivy,android

# Android settings
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.arch = arm64-v8a, armeabi-v7a
android.enable_androidx = True

# Uncomment this if you want a custom icon later
# icon.filename = %(source.dir)s/data/icon.png
