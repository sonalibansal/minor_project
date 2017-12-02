import MySQLdb

class DatabaseInteractor(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","123456","minorproject" )
		self.curs=self.db.cursor()

	def insert(self,user_name,date,time,address):
		
		try:
			sql = "SELECT userid from `user` WHERE username = '%s' " %(user_name)
			self.curs.execute(sql)
			result = self.curs.fetchone()
			if not self.curs.rowcount:
				
				try:
					print "here"	
					sql = "INSERT INTO `user`(username) VALUES ('%s')"%(user_name)
					print sql
					self.curs.execute(sql)
					self.db.commit()
					sql = "SELECT userid from `user` WHERE username = '%s' "%(user_name)
					print sql
					self.curs.execute(sql)
					result = self.curs.fetchone()
				except Exception as e:
					raise e
								
		except Exception as e:
			raise e	
			
		user_id = result[0]
		try:
			sql = "INSERT INTO `extract`(`userid`,`date`,`time`,`address`) VALUES (%d,'%s','%s','%s')"%(user_id,date,time,address)
			self.curs.execute(sql)	
			self.db.commit()
		except Exception as e:
			raise e

		