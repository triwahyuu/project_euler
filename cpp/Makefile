# $@ means the target of current rule
# $^ means all dependencies of current rule
# $< means first dependencies of current rule
CXX = g++ 
CXXFlags = -std=c++14
SRC = $(wildcard *.cpp)
EXE = $(patsubst %.cpp, $(BUILD_DIR)/%, $(SRC))
BUILD_DIR = build

all : $(EXE)

$(BUILD_DIR)/% : %.cpp euler.h utils.h Makefile
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFlags) $< -o $@ 

.PHONY : clean
clean :
	rm -f build/*