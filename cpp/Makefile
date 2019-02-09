# $@ means the target of current rule
# $^ means all dependencies of current rule
# $< means first dependencies of current rule
CXX = g++ 
CXXFlags = -std=c++11
SRC = $(wildcard *.cpp)
BUILD_DIR = build

all : $(patsubst %.cpp,$(BUILD_DIR)/%,$(SRC))

$(BUILD_DIR)/% : %.cpp euler.h utils.h
	@$(CXX) $(CXXFlags) $< -o $@ 

$(BUILD_DIR)/euler.o : euler.cpp
	$(CXX) $(CXXFlags) $< -c -o $@

.PHONY : clean
clean :
	rm -f build/*