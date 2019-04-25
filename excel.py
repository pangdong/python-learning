import io
import sys
import xlrd

#参考网站 http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html

def open_excel(file= 'file.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print (str(e))

def main():
	data = open_excel("test.xlsx")
	tables = data.sheets()[0]
	print(tables.nrows)
	print(tables.ncols)
	for rownum in (1,tables.nrows):
		row = tables.row_values(rownum)
		for colnum in (1,tables.ncols):
			print(row[colnum])

if __name__=="__main__":
	main()