project ('luabot', ['cpp', 'c'], 
    version : '0.0.1',
    meson_version : '>= 1.4.0',
    license : 'BSD',
    default_options: [
        'b_ndebug=if-release',
        'buildtype=release',
        'c_std=c99',
        'cpp_std=c++20',
    ])

fs = import ('fs')

c = meson.get_compiler ('c')
cpp = meson.get_compiler ('cpp')

boost_dep = dependency ('boost', required : false)

hal_dep      = dependency ('hal', method: 'cmake', required: true)
ntcore_dep   = dependency ('ntcore', method: 'cmake', required: true)
wpiutil_dep  = dependency ('wpiutil', method: 'cmake', required: true)
wpimath_dep  = dependency ('wpimath', method: 'cmake', required: true)
wpilibc_dep  = dependency ('wpilibc', method: 'cmake', required: true)
apriltag_dep = dependency ('apriltag', method: 'cmake', required: true)
cameraserver_dep = dependency ('cameraserver', method: 'cmake', required: true)
cscore_dep   = dependency ('cscore', method: 'cmake', required: true)
newcommands_dep = dependency ('wpilibnewcommands', method: 'cmake', required: true)

# TODO: these should be dynamic and/or option-ized
frc_platform = 'linuxx86-64'
frc_buildtype = 'release'
frc_libdir = meson.project_source_root() / 'build/install/frcUserProgram/linuxx86-64/release/lib'
frc_is_sim = true

phoenix6libs = []
phoenix6_sonames = '''
    CTRE_SimVictorSPX
    CTRE_SimProPigeon2
    CTRE_SimPigeonIMU
    CTRE_SimProCANcoder
    CTRE_SimProCANrange
    CTRE_SimProTalonFX
    CTRE_SimTalonSRX
    CTRE_SimCANCoder
'''.split()

if frc_is_sim
    phoenix6_sonames += [ 'CTRE_Phoenix6_WPISim', 'CTRE_PhoenixTools_Sim' ]
endif

foreach lib: phoenix6_sonames
    phoenix6libs += cpp.find_library (lib, 
        dirs: [ meson.project_source_root() / 'build/install/frcUserProgram/linuxx86-64/release/lib' ], required: true)
endforeach

phoenix6_dep = declare_dependency (
    include_directories: fs.expanduser ('~/SDKs/include'),
    dependencies: phoenix6libs
)

wpilib_deps = [ wpilibc_dep, newcommands_dep, phoenix6_dep ]

subdir ('src')
subdir ('test')
