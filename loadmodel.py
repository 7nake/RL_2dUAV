import matlab.engine
eng = matlab.engine.start_matlab()
c = eng.add(1, 2)
print(c)