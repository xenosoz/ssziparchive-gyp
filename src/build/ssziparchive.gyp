{
  'variables': {
    'MODULE_DEPTH': '..',
  },
  'conditions': [
    [
      'OS!="ios"', {
        'variables': {
          'SHARED_LIBRARY': 'shared_library',
        },
      },
    ],
    [
      'OS=="ios"', {
        'variables': {
          'SHARED_LIBRARY': 'static_library',
        },
        'xcode_settings': {
          'SDKROOT': 'iphoneos',
        },
      },
    ],
  ],
  'targets': [
    {
      'target_name': 'ssziparchive',
      'type': '<(SHARED_LIBRARY)',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(MODULE_DEPTH)/ssziparchive/',
        ],
      },
      'link_settings': {
        'libraries': [
          'libz.dylib',
        ],
      },
      'sources': [
        '<(MODULE_DEPTH)/ssziparchive/SSZipArchive.h',
        '<(MODULE_DEPTH)/ssziparchive/SSZipArchive.m',
        '<(MODULE_DEPTH)/ssziparchive/minizip/crypt.h',
        '<(MODULE_DEPTH)/ssziparchive/minizip/ioapi.c',
        '<(MODULE_DEPTH)/ssziparchive/minizip/ioapi.h',
        '<(MODULE_DEPTH)/ssziparchive/minizip/mztools.c',
        '<(MODULE_DEPTH)/ssziparchive/minizip/mztools.h',
        '<(MODULE_DEPTH)/ssziparchive/minizip/unzip.c',
        '<(MODULE_DEPTH)/ssziparchive/minizip/unzip.h',
        '<(MODULE_DEPTH)/ssziparchive/minizip/zip.c',
        '<(MODULE_DEPTH)/ssziparchive/minizip/zip.h',
      ],
    },
  ],
}
