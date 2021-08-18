if __name__ == "__main__":

	for i in range(10000):
		f = open("./tmp/"+ str(i) + ".txt", "w+")
		f.write(str(i))
		f.close()