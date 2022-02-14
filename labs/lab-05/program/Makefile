#all is triggered when make occurs, essentially runs makedir, static_block, and dynamic_block
all: makedir static_block dynamic_block

#make clean removes bin folder
clean:
	rm -rf bin/

#make directory to store files in
makedir:
	mkdir bin/
	mkdir bin/static
	mkdir bin/shared

#compile program
programcomp:
	gcc -c program.c -o bin/program.o

#make object static
staticobject:
	gcc -c source/block.c -o bin/static/block.o

#make object shared using fPIC flag
sharedobject:
	gcc -c -fPIC source/block.c -o bin/shared/block.o

#make lib, staticobject rule, meaning bin/static/block.o required beforehand
staticlib: staticobject
	ar rcs bin/static/libst.a bin/static/block.o

#make lib, sharedobject rule.
sharedlib: sharedobject
	gcc -shared bin/shared/block.o -o bin/shared/libsh.so

#link library with following rules
static_block: staticlib staticobject programcomp
	gcc bin/program.o -Lbin/static -lst -o bin/static_block

#link library with following rules, rpath set so LB_LIBRARY_PATH is exported
dynamic_block: sharedlib sharedobject programcomp
	gcc bin/program.o -Lbin/shared -lsh -Wl,-rpath=bin/shared -o bin/dynamic_block
