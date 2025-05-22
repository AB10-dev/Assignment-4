try:
    print('Reading file content: ')
    file1= open('sample.txt','r')
    reading_file_line1= file1.readline()
    reading_file_line2= file1.readline()
    print('Line 1: ',reading_file_line1)
    print('Line 2: ',reading_file_line2)
    file1.close()
except FileNotFoundError:
    print("Error:  The file '{file1}' was not found.")
