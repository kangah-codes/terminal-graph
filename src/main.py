import time
import psutil
import os
import terminalplot

x = range(100)
y = []

def main():
	while True:
		y.append(psutil.cpu_percent())
		terminalplot.plot(x, y)
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()
