import platform

print(platform.system())
# Darwin

print(platform.platform())
# macOS-10.15.7-x86_64-i386-64bit

print(platform.platform(aliased=True))
# macOS-10.15.7-x86_64-i386-64bit

print(platform.platform(terse=True))
# macOS-10.15.7

print(platform.version())
# Darwin Kernel Version 19.6.0: Tue Jan 12 22:13:05 PST 2021; root:xnu-6153.141.16~1/RELEASE_X86_64

print(platform.release())
# 19.6.0

print(platform.mac_ver())
# ('10.15.7', ('', '', ''), 'x86_64')

print(platform.win32_ver())
# ('', '', '', '')