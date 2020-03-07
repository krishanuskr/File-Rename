import os
# Function to rename multiple files
def main():
   i = 0
   path=r"C:/Users/atlas/Downloads/Music Videos/x/"
   for filename in os.listdir(path):
      my_source =path + filename
      my_dest=" "
      x=" "
      if filename.startswith("y2mate.com - "):
         x = filename[13:]
         my_dest = path + x
      else:
         my_dest = path +filename
      
      os.rename(my_source, my_dest)
      i += 1

if __name__ == '__main__':
   # Calling main() function
   main()
