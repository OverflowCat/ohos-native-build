def build() :
    return {
        'name': 'zlib',
        'commands': """
win:
    if not exist "zlib" (
      git clone https://github.com/madler/zlib.git
    )
    if not exist "output" mkdir output
    cd output
    if exist "zlib-%ARCH%-build" rmdir /S /Q zlib-%ARCH%-build
    mkdir zlib-%ARCH%-build
    cd zlib-%ARCH%-build
        
    cmake ../../zlib ^
        -G Ninja ^
        -DCMAKE_TOOLCHAIN_FILE="%OHOS_CMAKE_TOOLCHAIN_FILE%" ^
        -DCMAKE_MAKE_PROGRAM="%OHOS_SDK%/native/build-tools/cmake/bin/ninja.exe" ^
        -DCMAKE_BUILD_TYPE=Release ^
        -DCMAKE_INSTALL_PREFIX=%USED_PREFIX%/zlib/%ARCH% ^
        -DBUILD_SHARED_LIBS=OFF
    cmake --build . -- %MAKE_THREADS_CNT%
    cmake --install .
    
    cd ..
    if exist "zlib-%ARCH%-build2" rmdir /S /Q zlib-%ARCH%-build2
    mkdir zlib-%ARCH%-build2
    cd zlib-%ARCH%-build2
    
    cmake ../../zlib ^
        -G Ninja ^
        -DCMAKE_TOOLCHAIN_FILE="%OHOS_CMAKE_TOOLCHAIN_FILE%" ^
        -DCMAKE_MAKE_PROGRAM="%OHOS_SDK%/native/build-tools/cmake/bin/ninja.exe" ^
        -DCMAKE_BUILD_TYPE=Release ^
        -DCMAKE_INSTALL_PREFIX=%USED_PREFIX%/%ARCH% ^
        -DBUILD_SHARED_LIBS=OFF
    cmake --build . -- %MAKE_THREADS_CNT%
    cmake --install .
unix:
    if [ ! -d "zlib" ] ; then
      git clone https://github.com/madler/zlib.git
      cd zlib
      git checkout 643e17b749
      cd ..
    fi
    rm -rf output/zlib-$ARCH-build
    mkdir -p output/zlib-$ARCH-build
    cd output/zlib-$ARCH-build
    
    ../../zlib/configure \\
        --static \\
        --prefix=$USED_PREFIX/zlib/$ARCH
    make $MAKE_THREADS_CNT
    make install
    ../../zlib/configure \\
        --static \\
        --prefix=$USED_PREFIX/$ARCH
    make install    
"""
    }